# 1. Cargar la bbdd con langchain
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///ecommerce.db")
from dotenv import load_dotenv
import streamlit as st

# 2. Importar las APIs

import os

# 3. Crear el LLM
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=st.secrets["OPENAI_API_KEY"])

# 4. Crear la cadena
from langchain.llms import OpenAI
cadena = SQLDatabaseChain.from_llm(OpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"]), db)

# 5. Formato personalizado de respuesta
formato = """
Data una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

# 6. Función para hacer la consulta

def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)
    resultado = cadena.run(consulta)
    return(resultado)