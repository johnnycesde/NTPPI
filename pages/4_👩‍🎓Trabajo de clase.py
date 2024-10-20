import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la Aplicación
st.title("Análisis de Datos sobre Estudiantes")

# Paso 1: Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Sofía', 'Carlos', 'María', 'Luis'],
    'Edad': [18, 19, 18, 17, 20, 18, 19],
    'Género': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Calificación': [8.5, 7.0, 9.2, 9.8, 6.5, 8.0, 7.8]
}

df = pd.DataFrame(data)
st.write("### Datos Originales", df)

# Paso 2: Agrupación por Género
grouped = df.groupby('Género')

# Paso 3: Resumen de Edad
edad_promedio = grouped['Edad'].mean()

# Paso 4: Resumen de Calificaciones
calificacion_promedio = grouped['Calificación'].mean()
calificacion_maxima = grouped['Calificación'].max()

# Paso 5: Tabla de Resumen
resumen = pd.DataFrame({
    'Edad Promedio': edad_promedio,
    'Calificación Promedio': calificacion_promedio,
    'Calificación Máxima': calificacion_maxima
}).reset_index()

st.write("### Tabla de Resumen", resumen)

# Preguntas adicionales
# 1. Cantidad de estudiantes por género
cantidad_estudiantes = grouped.size()
st.write("### Cantidad de Estudiantes por Género", cantidad_estudiantes)

# 2. Ordenar la tabla de resumen por la calificación promedio de forma descendente
resumen_ordenado = resumen.sort_values(by='Calificación Promedio', ascending=False)
st.write("### Tabla de Resumen Ordenada por Calificación Promedio", resumen_ordenado)

# 3. Agregar una nueva columna al DataFrame con la categoría de edad
df['Categoría Edad'] = df['Edad'].apply(lambda x: 'Joven' if x < 19 else 'Adulto')
st.write("### DataFrame con Categoría de Edad", df)

# Gráficos en Streamlit
# 1. Gráfico de dispersión de calificaciones
st.write("### Distribución de Calificaciones por Género")
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Género', y='Calificación')
plt.title('Distribución de Calificaciones por Género')
plt.xlabel('Género')
plt.ylabel('Calificación')
st.pyplot(plt)

# 2. Gráfico de barras de edad y calificación promedio
st.write("### Edad y Calificación Promedio por Género")
plt.figure(figsize=(10, 5))
resumen.set_index('Género')[['Edad Promedio', 'Calificación Promedio']].plot(kind='bar')
plt.title('Edad y Calificación Promedio por Género')
plt.xlabel('Género')
plt.ylabel('Promedio')
plt.xticks(rotation=0)
st.pyplot(plt)

# 3. Gráfico de pastel para mostrar la proporción de estudiantes por género
st.write("### Proporción de Estudiantes por Género")
plt.figure(figsize=(8, 6))
cantidad_estudiantes.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Proporción de Estudiantes por Género')
plt.ylabel('')
st.pyplot(plt)
