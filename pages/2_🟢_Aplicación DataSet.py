import streamlit as st 
import pandas as pd
from faker import Faker
import random
import google.generativeai as genai

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

# Cargar el archivo CSV
try:
    df = pd.read_csv('C:/Users/Johny/Desktop/tableConvert.com_1ct0y2.csv', delimiter='|')
    if df.empty:
        st.error("El archivo CSV está vacío o no contiene datos.")
    else:
        st.success("Datos cargados correctamente.")
except FileNotFoundError:
    st.error("El archivo no fue encontrado.")
    df = pd.DataFrame()  # Crear un DataFrame vacío si el archivo no se encuentra
except pd.errors.EmptyDataError:
    st.error("El archivo está vacío.")
    df = pd.DataFrame()  # Crear un DataFrame vacío si no hay datos
except pd.errors.ParserError:
    st.error("Error al analizar el archivo. Verifica el delimitador y el formato.")
    df = pd.DataFrame()  # Crear un DataFrame vacío en caso de error
except Exception as e:
    st.error(f"Ocurrió un error inesperado: {e}")
    df = pd.DataFrame()  # Crear un DataFrame vacío en caso de error

# Crear pestañas
tab_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico, tab_Generador, tab_Gemini = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico", "Generador", "Gemini"])

#----------------------------------------------------------
# Generador de datos
#----------------------------------------------------------
with tab_descripcion:      
    st.markdown('''...''')  # Aquí va tu descripción

with tab_Generador: 
    st.write('Esta función genera datos ficticios de usuarios y los guarda en un archivo CSV.')
    
    # Inicializar Faker para Colombia
    fake = Faker('es_CO')

    # Lista de programas técnicos
    programas_tecnicos = [
        'Técnico en Programación', 'Seguridad y Salud en el Trabajo', 
        'Diseño Gráfico', 'Técnico en Contabilidad'
    ]

    # Función para generar usuarios ficticios
    def generate_fake_usuarios(n):
        usuarios = []
        for _ in range(n):
            user = {
                'Nombre': fake.name(),
                'Edad': random.randint(18, 80),
                'Programa de Estudio': random.choice(programas_tecnicos),
                'Fecha de Reserva': fake.date_between(start_date='-30d', end_date='today'),
                'Hora de Reserva': fake.time()
            }
            usuarios.append(user)
        return usuarios
    
    st.subheader("Generar Usuarios Ficticios")

    # Generar datos ficticios
    num_users = st.number_input("Número de usuarios a generar:", min_value=1, max_value=100, value=60)
    
    fake_users = []  # Inicializa la variable antes de usarla

    if st.button("Generar Usuarios"):
        fake_users = generate_fake_usuarios(num_users)
        
        # Crear el DataFrame y mostrar datos generados
        df_fake = pd.DataFrame(fake_users)

        # Mostrar el DataFrame en Streamlit
        st.dataframe(df_fake)

        # Guardar el DataFrame en un archivo CSV
        df_fake.to_csv('C:/Users/Johny/Desktop/tableConvert.com_1ct0y2.csv', sep='|', index=False)
        st.success("Archivo CSV generado exitosamente.")

#----------------------------------------------------------
# Análisis Exploratorio
#----------------------------------------------------------
def analisis_exploratorio(df):
    if df.empty:
        st.error("El DataFrame está vacío. No se puede realizar el análisis.")
        return
    
    consultas_seleccionadas = st.multiselect('Selecciona las consultas que quieres realizar:', [
        "Muestra las primeras 5 filas",
        "Muestra la cantidad de filas y columnas",
        "Muestra los tipos de datos",
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

# Llama a la función para ejecutar el análisis exploratorio en la pestaña correspondiente
with tab_Análisis_Exploratorio:
    st.title("Análisis Exploratorio")
    analisis_exploratorio(df)  # Asegúrate de pasar 'df' aquí

#----------------------------------------------------------
# Filtrado Básico
#----------------------------------------------------------
with tab_Filtrado_Básico:
    st.title("Filtro Básico")
    st.markdown("""...""")  # Aquí va tu explicación sobre el filtro básico

    # Implementación del filtro básico
    
    columna_filtro = st.selectbox("Selecciona una columna para filtrar:", df.columns if not df.empty else [])
    valor_filtro = st.text_input("Introduce el valor para filtrar:")
    operador = st.radio("Selecciona un operador de comparación:", options=["Igual", "Diferente", "Mayor que", "Menor que"])
    
    # Verificar el tipo de dato de la columna seleccionada
    if not df.empty and columna_filtro:
        tipo_columna = df[columna_filtro].dtype

        if st.button("Aplicar filtro"):
            # Convertir el valor de filtro a un número si la columna es numérica
            if pd.api.types.is_numeric_dtype(tipo_columna):
                try:
                    valor_filtro = float(valor_filtro)  # Convertir a float para comparación
                except ValueError:
                    st.error("Introduce un número válido para el filtro.")
                    valor_filtro = None  # Reiniciar valor_filtro si no es válido

            # Aplicar el filtro solo si valor_filtro es válido
            if valor_filtro is not None:
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
            else:
                st.error("No se pudo aplicar el filtro debido a un valor inválido.")
    else:
        st.error("No hay datos disponibles para filtrar.")
#----------------------------------------------------------
# Filtro Final Dinámico
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
    st.title("Filtro Final Dinámico")
    st.markdown("""...""")  # Aquí va tu explicación sobre el filtro final dinámico

    # Mostrar el DataFrame filtrado (asegúrate de que df_filtrado esté disponible)
    if 'df_filtrado' in locals():
        st.subheader("Resumen del DataFrame Filtrado:")
        st.write(f'Total de filas después del filtro: {df_filtrado.shape[0]}')
        st.dataframe(df_filtrado)

        # Gráficos y estadísticas relevantes
        st.subheader("Resumen Estadístico de Datos Filtrados:")
        st.write(df_filtrado.describe())


#----------------------------------------------------------
# IA
#----------------------------------------------------------
with tab_Gemini:      
    st.markdown('''...''')  # Aquí va tu descripción

with tab_Gemini: 
    st.write('Esta función es la IA aplicada a nuestro proyecto')

    #Aplicación de la IA 
    
genai.configure(api_key="AIzaSyAv1hilQoodq8NGkxzOmX_2Pq7uNkz7b_8")

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = st.text_input("Preguntar")
if st.button("Preguntar"):

    response = model.generate_content(prompt)
    st.write(response.text)
    

