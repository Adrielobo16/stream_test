# Parte 1 - Importar librerías 
import streamlit as st                                              # Librería para Streamlit
import pandas as pd
import numpy as np 

# Parte 2 - Configuraciones iniciales
st.set_page_config(                                                 # Nombre a la página
    page_title = "Monitoreo Industrial",
    layout = "wide" 
)

st.title("Sistema de Monitoreo Industrial")                         # Titulo de la página
st.write("Bienvenido al Sistema de Monitoreo en Tiempo Real")       # Texto de la página