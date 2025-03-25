# Data Base Query

[![Screenshot-from-2025-03-25-16-00-25.png](https://i.postimg.cc/R0Hz1H15/Screenshot-from-2025-03-25-16-00-25.png)](https://postimg.cc/zL8M83P0)

Esta herramienta es un modelo NL2SQL, la cual recibe lenguaje natural y lo transforma a SQL para comunicarse con una base de datos. Esta base de datos es de prueba, y solo muestro 10 filas para que no se ralentize la carga, como ejemplo. Todo el codigo esta en mi Github. Para cualquier problema o propuesta: juanglezm3@gmail.com

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Vas a necesitar una api-key:

* [OpenAI Api-Key](https://openai.com/index/openai-api/) -> Enlace para obtenerla.

En primer lugar crea un archivo .env, ahí guardaras tu clave con el siguiente par clave valor:

* OPENAI_API_KEY = "tu_api_key" (esta será tu api_key de OpenAI, no cambies el nombre)

Crea un archivo .env en el directorio /backend, y guarda esta clave ahí.

### Pre-requisitos 📋

Todos los requerimientos estan en requirements.txt:
```bash
  pip install -r requirements.txt
```
He utilizado python 3.12.3, para perfecta compatibilidad utilizar misma versión.

### Instalación 🔧

_Creamos un virtual environment_

_Linux/MacOS:_

```
python3 -m venv nombre_venv
source nombre_venv/bin/activate
pip install -r /backend/requirements.txt
python3 /backend/app.py
```

_Windows_

```
python3 -m venv nombre_venv
nombre venv\Scripts\activate.bat
pip install -r \backend\requirements.txt
python3 \backend\app.py
```

_Ya tendrias la herramienta corriendo en tu maquina local_

## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/stable/) - El framework web usado
* [LangChain](https://www.langchain.com/) - Integracion y uso de LLMS
* [sqlite3](https://www.sqlite.org/) - Comunicacion del backend con la base de datos

## Licencia 📄

Mira el archivo [LICENSE.md](LICENSE.md) para detalles. Si quieres usar esta herramienta para tu uso personal, agrega un enlace a este repositorio en tu readme por favor. Espero que sea de utilidad.

## Mis redes sociales 🌐

* Comenta a otros sobre este proyecto 📢
* Mis redes sociales son: 
* [Tiktok](https://www.tiktok.com/@jgmdev) 
* [Linkedin](https://www.linkedin.com/in/jgmdatascience/) 






