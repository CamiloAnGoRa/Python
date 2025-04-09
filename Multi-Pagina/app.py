import pandas as pd
import streamlit as st
import plotly.express as px


#Funcion pagina principal
def pagina_principal():
    #Titulo de la pagina
    st.title("Pagina Principal")
    #Parrafos st.write
    st.write("Bienvenido a la aplicacion de demostracion")
    st.write("Usa el menú de la izquierda para navegar entre las distintas paginas")


#Funcion visualizador de datos
def Visualizacion_Datos():
    st.title("Visualizacion de datos")
    st.write("Selecciona el archivo que deseas observar los datos (formato CSV)")


    #Declariacion de varialble para guardado de archivo, solicita un archivo de formato csv
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv")


    #Si la variable ya almace un archivo muestra los datos de lo contrario no muestra nada
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo CSV: ")
        st.write(df)
        st.write("Estadisticas descriptivas: ")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Graficos Interactivos")
    st.write("Carga un archivo CSV para generar el grafico")
    #con el key evitamos posibles interferencias con la anterior variable de la otra funcion
    archivo_carado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")

    if archivo_carado is not None:
        df = pd.read_csv(archivo_carado)
        st.write("Elige una columna para el eje X: ")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elige una columna para el eje Y: ")
        eje_y = st.selectbox("Eje Y", df.columns)

        if st.button("Crear Grafico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)


#Creacion la barra lateral de navegación
st.sidebar.title("Navegación")


#Declaracion de variable pagina donde se selecciona la pagina a la que se accedera
pagina = st.sidebar.selectbox("Selecciona la pagina a la que quiere acceder", 
                                ["Pagina principal", 
                                "Visualizador de datos",
                                "Graficacion de datos"])


#Hacemos el llamado de la apgina principal en caso de que sea la seleccionada
if pagina == "Pagina principal":
    pagina_principal()

elif pagina == "Visualizador de datos":
    Visualizacion_Datos()

elif pagina == "Graficacion de datos":
    graficos_interactivos()