import streamlit as st

# Título de la aplicación
st.title('Autocompletado de Frases con Selector')

# Lista de opciones predefinidas
options = ["Hola, ¿cómo estás?", "¿Qué tal tu día?", "¡Bienvenido a Streamlit!"]
selected_texts = st.session_state.get('selected_texts', [])

# Selector de opciones
selected_option = st.selectbox("Selecciona una opción:", options)

# Botón para añadir la opción seleccionada a la frase
if st.button("Agregar a la frase"):
    selected_texts.append(selected_option)
    st.session_state['selected_texts'] = selected_texts

# Mostrar la frase autocompletada
autocompleted_text = " ".join(selected_texts)
st.write("Frase autocompletada:")
st.write(autocompleted_text)

# Botón para borrar elementos de la frase
if st.button("Borrar último elemento"):
    if len(selected_texts) > 0:
        selected_texts.pop()
        st.session_state['selected_texts'] = selected_texts




#         Prompt: Hey ChatGPT, I am a software developer focusing on creating accessible applications to enhance the lives of individuals with disabilities. I aim to assist users with mobility challenges and specific needs, by addressing the lack of accessible solutions that hinder their independence. Common obstacles include limited accessibility, high costs, and neglect of user-specific requirements.

# I am planning to develop customizable tools with user-friendly interfaces and innovative features to support daily living for users. Previous attempts lacked adaptability, accessibility, and alignment with unique user needs. My end goals are to boost independence, encourage broad adoption, and gather valuable feedback for ongoing development.

# Develop a Streamlit prototype that allows users to select multiple options from a dropdown menu and cumulatively build a sentence. The users should be able to add elements to the sentence without deleting the existing ones, unless they opt to remove specific elements. The main objective is to provide an interactive approach for users to construct sentences based on their selections.