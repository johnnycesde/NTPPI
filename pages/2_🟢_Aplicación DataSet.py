import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

df = pd.read_csv('./static/datasets/ventas.csv')


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''
    ## Plantilla Básica para Proyecto Integrador

    ### Introducción

    -   ¿Qué es el proyecto?
                RESERVAS DE SALAS DE ESTUDIO
    -   ¿Cuál es el objetivo principal?
    -   ¿Por qué es importante?

    ### Desarrollo

    -   Explicación detallada del proyecto
    -   Procedimiento utilizado
    -   Resultados obtenidos

    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    ''')    

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    
    st.title("Análisis Exploratorio")
    st.markdown("""
    * Muestra las primeras 5 filas del DataFrame.  **(df.head())**
    * Muestra la cantidad de filas y columnas del DataFrame.  **(df.shape)**
    * Muestra los tipos de datos de cada columna.  **(df.dtypes)**
    * Identifica y muestra las columnas con valores nulos. **(df.isnull().sum())**
    * Muestra un resumen estadístico de las columnas numéricas.  **(df.describe())**
    * Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada. **(df['columna_categorica'].value_counts())** 
    * Otra información importante           
    """)   
    
#----------------------------------------------------------
#Analítica 2
def analisis_exploratorio(df):
 df = pd.read_csv('./static/datasets/reserva_salas_estudio_60_usuarios.csv')


# selector multi-select para que el usuario elija las consultas
consultas_seleccionadas = st.multiselect('Selecciona las consultas que quieres realizar:',[
      "Muestra las primeras 5 filas",
      "Muestra la cantidad de filas y columnas",
      "Muestra lo tipos de datos",
      "Identifica y muestra las columnas con valores nulos",
      "Muestra un resumen estadístico de las columnas numéricas",
      "Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada"
        
])

# Ejecutar las consultas seleccionadas
  
if consultas_seleccionadas:
    for consulta in consultas_seleccionadas:
         if consulta == "Muestra las primeras 5 filas":
              st.dataframe(df.head(5))
         elif consulta == "Muestra la cantidad de filas y columnas":
                st.subheader("Cantidad de filas y columnas:")
                st.write(f'Filas: {df.shape[0]}, Columnas: {df.shape[1]}')
         elif consulta == "Muestra los tipos de datos":
                st.subheader("Tipos de datos de cada columna:")
                st.write(df.dtypes)
         elif consulta == "Identifica y muestra las columnas con valores nulos":
                st.subheader("Columnas con valores nulos:")
                st.write(df.isnull().sum())
         elif consulta == "Muestra un resumen estadístico de las columnas numéricas":
                st.subheader("Resumen estadístico:")
                st.write(df.describe())
         elif consulta == "Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada":
                columna = st.selectbox("Selecciona una columna categórica:", df.select_dtypes(include=['object']).columns)
                if columna:
                    frecuencia = df[columna].value_counts().reset_index()
                    frecuencia.columns = [columna, 'Frecuencia']
                    st.subheader(f"Frecuencia de valores únicos en '{columna}':")
                    st.dataframe(frecuencia)

# Llama a la función para ejecutar el análisis exploratorio
if __name__ == "__main__":
    analisis_exploratorio()

with tab_Filtrado_Básico:
        st.title("Filtro Básico")
        st.markdown("""
        * Permite filtrar datos usando condiciones simples. **(df[df['columna'] == 'valor'])**
        * Permite seleccionar una columna y un valor para el filtro. **(st.selectbox, st.text_input)**
        * Permite elegir un operador de comparación (igual, diferente, mayor que, menor que). **(st.radio)**
        * Muestra los datos filtrados en una tabla. **(st.dataframe)** 
        """)

#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------
# Implementación del filtro básico
columna_filtro = st.selectbox("Selecciona una columna para filtrar:", df.columns)
valor_filtro = st.text_input("Introduce el valor para filtrar:")
operador = st.radio("Selecciona un operador de comparación:", options=["Igual", "Diferente", "Mayor que", "Menor que"])
    
if st.button("Aplicar filtro"):
        if operador == "Igual":
            df_filtrado = df[df[columna_filtro] == valor_filtro]
        elif operador == "Diferente":
            df_filtrado = df[df[columna_filtro] != valor_filtro]
        elif operador == "Mayor que":
            df_filtrado = df[df[columna_filtro] > valor_filtro]
        elif operador == "Menor que":
            df_filtrado = df[df[columna_filtro] < valor_filtro]

        st.subheader("Datos Filtrados:")
        st.dataframe(df_filtrado)

# Filtro Final Dinámico
with tab_Filtro_Final_Dinámico:
     st.title("Filtro Final Dinámico")
     st.markdown("""
    * Muestra un resumen dinámico del DataFrame filtrado. 
    * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
    * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
    """)

    # Mostrar el DataFrame filtrado (asegúrate de que df_filtrado esté disponible)
if 'df_filtrado' in locals():
        st.subheader("Resumen del DataFrame Filtrado:")
        st.write(f'Total de filas después del filtro: {df_filtrado.shape[0]}')
        st.dataframe(df_filtrado)

        # Gráficos y estadísticas relevantes
        st.subheader("Resumen Estadístico de Datos Filtrados:")
        st.write(df_filtrado.describe())
        
        # Si deseas agregar gráficos, puedes usar matplotlib o seaborn aquí

# Llama a la función para ejecutar el análisis exploratorio
if __name__ == "__main__":
     analisis_exploratorio()
         