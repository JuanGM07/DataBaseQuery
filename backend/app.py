from flask import Flask, request, jsonify, render_template
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

DATABASE_PATH = "/home/juangm/Code/pythonProjects/DataBaseQuery/backend/ecommerce.db"
# Crear el motor de conexión con SQLAlchemy
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
# Crear el objeto db
db = SQLDatabase.from_uri(f"sqlite:///{DATABASE_PATH}")

# Configurar el modelo de lenguaje
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Asegúrate de configurar esto en tu entorno
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
cadena = SQLDatabaseChain.from_llm(llm, db)

# Función para obtener las primeras 20 filas de la base de datos
def get_first_20_rows():
    conn = sqlite3.connect(DATABASE_PATH)
    query = "SELECT * FROM ventas LIMIT 20"  # Cambia 'ventas' por el nombre de tu tabla
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df.to_html(classes="table table-striped")

# Página principal
@app.route('/')
def index():
    # Obtener las primeras 20 filas de la base de datos
    db_table = get_first_20_rows()
    return render_template('index.html', db_table=db_table)

# Endpoint para hacer consultas
@app.route('/consulta', methods=['POST'])
def consulta():
    try:
        data = request.get_json()
        user_query = data.get("query", "")

        # Si no se proporciona una consulta, devolver un error
        if not user_query:
            return jsonify({"error": "No se proporcionó ninguna consulta"}), 400

        # Reformulación del prompt para que el modelo genere una respuesta
        formato = """
        Data una pregunta del usuario:
        1. crea una consulta de sqlite3
        2. revisa los resultados
        3. devuelve el dato
        4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
        #{question}
        """
        consulta_sql = formato.format(question=user_query)

        # El modelo genera la respuesta, incluyendo una consulta SQL que no ejecutamos
        response = cadena.invoke(consulta_sql)

        # Extraer solo el 'result' de la respuesta
        result = response.get("result", "")

        # Verificar que el 'result' no esté vacío
        if not result:
            return jsonify({"error": "No se generó una respuesta válida del modelo"}), 400

        # Devolver la respuesta generada (solo el 'result' que es la respuesta final)
        return jsonify({"response": result})

    except Exception as e:
        # Manejo de errores
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
