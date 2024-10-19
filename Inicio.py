import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("Proyecto Integrador: [Nombre del Proyecto]")
st.subheader("Un Viaje Creativo con [Nombre del Equipo]")

# Imagen de fondo
image = Image.open("./static/proyecto integrador.png") 
st.image(image, width=700, use_column_width=True)  

# Integrantes
st.header("Nuestro Equipo")

col1, col2 = st.columns(2)

with col1:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[SARA LOPERA]**")
    st.write("[Rol en el proyecto]")

with col2:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[MIGUEL ROLDAN]**")
    st.write("[Rol en el proyecto]")

with col1:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[ALEXANDER HERNANDEZ]**")
    st.write("[Rol en el proyecto]")  

with col2:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[JOHNNY LONDOÑO ]**")
    st.write("[Rol en el proyecto]")   

# Descripción del proyecto
st.header("RESERVAS DE SALAS DE ESTUDIO")
st.write("""
[La aplicación "Reserva de Salones de Estudio" facilita la organización y gestión de espacios de estudio, ofreciendo a los usuarios la posibilidad de reservar salones de manera rápida y eficiente. El objetivo principal es optimizar el uso de estos espacios, eliminando conflictos por disponibilidad y brindando una experiencia ágil y cómoda para estudiantes y profesionales. Aborda el problema de la falta de coordinación en la asignación de salones, permitiendo consultar la disponibilidad en tiempo real y realizar reservas con un solo clic. El enfoque se basa en una interfaz intuitiva y amigable, diseñada para facilitar la navegación y mejorar la experiencia del usuario..]
""")

# Más información
st.header("Más Información")

# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas

st.write("""
[Agrega la información adicional que consideres relevante.]
""")

# Footer con links
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.google.com">Google</a> |
        <a href="https://www.facebook.com">Facebook</a> |
        <a href="https://www.linkedin.com">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)