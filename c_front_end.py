#lanzar con streamlit run c_front_end.py en el terminal

import b_backend
import streamlit as st
from streamlit_chat import message
import pandas as pd
import sqlite3

icono='149206.png'
logo='cover.png'
st.set_page_config(page_title='Data Base Query',
                   page_icon=icono)
conn=sqlite3.connect('ecommerce.db')
query='SELECT * FROM ventas'
df=pd.read_sql_query(query,conn)
st.sidebar.table(df)
st.image(image=logo,width=None)
st.divider()
st.title("Data Base Query")
st.write("You can ask me all you want about the database")

if 'preguntas' not in st.session_state:
    st.session_state['preguntas'] = []
if 'respuestas' not in st.session_state:
    st.session_state['respuestas'] = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ''

with st.form('my-form'):
 
   query = st.text_input('¿How can I help you?:', key='user', help='Press Send to ask the question')
   submit_button = st.form_submit_button('Send',on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas)-1, -1, -1):
        message(st.session_state.respuestas[i], key=str(i))

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('¿Do you want to do another question?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []









