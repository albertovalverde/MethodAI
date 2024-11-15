import streamlit as st

# Initialize the sentence
sentence = ""

# Define the fragmented options for the dropdown menu
option_fragments = [
    "La atención fue excelente,",
    "La atención fue muy buena,",
    "La atención fue buena,",
    "La atención fue aceptable,",
    "La atención fue deficiente,",
    "El personal fue extremadamente amable y atento,",
    "El personal brindó un servicio excepcional,",
    "El personal fue eficiente y profesional,",
    "Esperaba un trato más cordial y profesional,",
    "El servicio careció de atención personalizada,",
    "Podría haber sido más atenta y eficiente,",
    "Encontré áreas en las que se puede mejorar:"
]

# Create a multiselect to allow users to select options
selected_options = st.multiselect("Select options:", option_fragments)

# Create a text input for users to add custom text
custom_text = st.text_input("Add custom text (optional)")

# Create a button to add the selected options and custom text to the sentence
if st.button("Add to sentence"):
    for option in selected_options:
        sentence += option + " "
    if custom_text:
        sentence += custom_text
    st.write(sentence)

# Create a button to remove specific elements from the sentence
if st.button("Remove elements"):
    sentence = ""
    for option in selected_options:
        if option not in option_fragments[:2]:  # Remove first two fragments
            sentence += option + " "
    if custom_text:
        sentence += custom_text
    st.write(sentence)

# prompt
# Por favor, proporcióname un código en Python que utilice la biblioteca Streamlit para crear una aplicación interactiva. El código debe incluir una lista de fragmentos de opciones, un multiselect que permita a los usuarios seleccionar elementos de la lista, un campo de texto para ingresar texto personalizado y botones que al presionarlos, agreguen las opciones seleccionadas junto con el texto personalizado a una variable 'sentence'. Además, debe haber un botón para eliminar elementos específicos de 'sentence', con la condición de que solo se eliminen los dos primeros elementos de la lista de opciones al seleccionar la opción eliminar

