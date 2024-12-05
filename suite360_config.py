import streamlit as st

# Función para mostrar etiqueta con ahorro de tiempo y pasos
def mostrar_etiqueta(tiempo_ahorrado, pasos_eliminados, detalles_pasos):
    st.markdown(
        f"""
        <div style="display: inline-block; margin-left: 10px; padding: 5px; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;">
            <strong>Beneficio:</strong> Ahorro de {tiempo_ahorrado}, eliminando {pasos_eliminados} pasos manuales.
            <br><strong>Detalles de los pasos ahorrados:</strong><br>{detalles_pasos}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Título principal
st.title("Ejemplo de Configuración Detallada de Activación del Servicio Alerta Legal 360°")

# Descripción del caso y cómo funciona Alerta Legal 360°
st.subheader("Configuración de la herramienta Alerta Legal 360°")
st.write("""
Alerta Legal 360° es una herramienta que automatiza la gestión de casos legales. A continuación, podrás configurar los diferentes componentes que integran este sistema, como el correo, calendario y gestor documental.
""")

# Descripción del caso con Alerta Legal 360°
st.subheader("Proceso con Alerta Legal 360°")
st.write("""
Cuando recibes un correo de un cliente confirmando una cita, Alerta Legal 360° extrae automáticamente la información relevante de ese correo y organiza los documentos necesarios. Además, te permite gestionar el calendario y los archivos de manera eficiente con la integración de diversos proveedores.
""")

# Panel para la configuración de Correo (IMAP)
with st.expander("Configuración de Correo (IMAP)") :
    correo_proveedor = st.selectbox("Selecciona el proveedor de correo:", ["Gmail", "Outlook", "Otro"])
    if correo_proveedor == "Otro":
        correo_direccion = st.text_input("Escribe la dirección de correo IMAP")
        st.text("Proporciona los detalles de configuración de IMAP para este proveedor.")
    st.write("Este proveedor se utilizará para extraer automáticamente los correos electrónicos de los clientes y gestionar la información relevante.")

# Panel para la configuración de Calendario
with st.expander("Configuración de Calendario"):
    calendario_proveedor = st.selectbox("Selecciona el proveedor del calendario:", ["Google Calendar", "Microsoft Outlook", "Otro"])
    if calendario_proveedor == "Otro":
        calendario_direccion = st.text_input("Escribe los detalles del calendario del proveedor seleccionado.")
    st.write("Este proveedor se utilizará para gestionar y sincronizar automáticamente las citas de los clientes.")

# Panel para la configuración de Gestor Documental
with st.expander("Configuración de Gestor Documental"):
    gestor_documental = st.selectbox("Selecciona el gestor documental:", ["Google Drive", "Dropbox", "Otro"])
    if gestor_documental == "Otro":
        gestor_direccion = st.text_input("Escribe los detalles de acceso al gestor documental.")
    st.write("Este proveedor se utilizará para organizar y almacenar los documentos relevantes del caso.")

# Panel para la acción de creación de automatización
st.header("Acción para crear la automatización")
st.write("""
Una vez configurados los proveedores, puedes proceder a crear la automatización para que Alerta Legal 360° comience a gestionar el caso de manera eficiente.
""")
if st.button("Crear Automatización de Alerta Legal 360°"):
    st.success("Automatización de Alerta Legal 360° creada exitosamente.")
    mostrar_etiqueta("1.5 horas por consulta", "4 pasos", "- Revisión manual de correos electrónicos\n- Organización de documentos\n- Coordinación manual de citas\n- Almacenamiento de documentos")



import streamlit as st

# Función para mostrar etiqueta con ahorro de tiempo y pasos
def mostrar_etiqueta(tiempo_ahorrado, pasos_eliminados, detalles_pasos):
    st.markdown(
        f"""
        <div style="display: inline-block; margin-left: 10px; padding: 5px; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;">
            <strong>Beneficio:</strong> Ahorro de {tiempo_ahorrado}, eliminando {pasos_eliminados} pasos manuales.
            <br><strong>Detalles de los pasos ahorrados:</strong><br>{detalles_pasos}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Título principal
st.title("Ejemplo de Configuración Detallada de Activación del Servicio AI Lead Booster")

# Descripción del caso y cómo funciona AI Lead Booster
st.subheader("Configuración de la herramienta AI Lead Booster")
st.write("""
AI Lead Booster es una herramienta automatizada que utiliza inteligencia artificial para capturar y gestionar leads de manera eficiente. A continuación, podrás configurar los diferentes componentes que integran este sistema, como las redes sociales, la plataforma de automatización y las integraciones con otros servicios.
""")

# Descripción del caso con AI Lead Booster
st.subheader("Proceso con AI Lead Booster")
st.write("""
AI Lead Booster automatiza el proceso de captura de leads mediante redes sociales y otras fuentes. La herramienta gestiona las interacciones, alimenta la base de datos de clientes potenciales y realiza el seguimiento adecuado para maximizar las conversiones. Los leads se capturan automáticamente y se gestionan a través de la plataforma de automatización integrada.
""")

# Panel para la configuración de Redes Sociales con opción de multiselección
with st.expander("Configuración de Redes Sociales"):
    redes_seleccionadas = st.multiselect(
        "Selecciona las redes sociales para capturar leads:",
        ["Facebook", "Instagram", "LinkedIn", "Twitter", "Otro"],
        default=["Facebook", "Instagram"]
    )
    if "Otro" in redes_seleccionadas:
        red_social_detalles = st.text_input("Escribe los detalles de la red social seleccionada.")
    st.write("Estas redes sociales se utilizarán para capturar automáticamente los leads mediante formularios o interacciones.")

# Panel para la configuración de la herramienta que generará los contenidos para las redes sociales
with st.expander("Configuración de Generador de Contenidos para Redes Sociales"):
    herramienta_contenidos = st.selectbox(
        "Selecciona la herramienta para generar los contenidos:",
        ["Google Forms", "Airtable", "Otro"]
    )
    
    if herramienta_contenidos == "Google Forms":
        st.text_input("Escribe el enlace de Google Form que se usará para capturar los contenidos.")
    elif herramienta_contenidos == "Airtable":
        st.text_input("Escribe el enlace de Airtable donde se gestionarán los contenidos.")
    elif herramienta_contenidos == "Otro":
        st.text_input("Escribe el enlace a la herramienta personalizada que se utilizará.")

    st.write("Este enlace será utilizado para buscar los contenidos a publicar en las redes sociales como parte del flujo de trabajo del agente IA.")

# Panel para la configuración de Base de Datos de Leads
with st.expander("Configuración de Base de Datos de Leads"):
    base_datos_proveedor = st.selectbox("Selecciona el proveedor de la base de datos de leads:", ["Google Sheets", "Airtable", "Otro"])
    if base_datos_proveedor == "Otro":
        base_datos_detalles = st.text_input("Escribe los detalles de la base de datos seleccionada.")
    st.write("Esta base de datos se utilizará para almacenar los leads capturados y gestionar su seguimiento.")

# Panel para la configuración del Agente IA que contactará al Lead (WhatsApp o Correo)
with st.expander("Configuración del Agente IA para Contactar Leads"):
    metodo_contacto = st.selectbox(
        "Selecciona el método de contacto del agente IA:",
        ["WhatsApp", "Correo Electrónico"]
    )

    if metodo_contacto == "Correo Electrónico":
        st.text_input("Escribe la dirección de correo desde la que se enviarán los mensajes:")
        st.text_area("Escribe el mensaje de correo predeterminado para contactar a los leads:")
    elif metodo_contacto == "WhatsApp":
        st.text_input("Escribe el número de teléfono de WhatsApp para contactar a los leads:")
        st.text_area("Escribe el mensaje predeterminado para WhatsApp:")

    st.write("El agente IA utilizará este método de contacto para enviar mensajes a los leads y realizar el seguimiento.")

# Panel para la acción de creación de automatización
st.header("Acción para crear la automatización")
st.write("""
Una vez configurados los proveedores, puedes proceder a crear la automatización para que AI Lead Booster comience a capturar y gestionar los leads de manera eficiente.
""")
if st.button("Crear Automatización de AI Lead Booster"):
    st.success("Automatización de AI Lead Booster creada exitosamente.")
    mostrar_etiqueta("2 horas por campaña", "6 pasos", "- Captura manual de leads\n- Clasificación de leads\n- Carga manual en base de datos\n- Respuesta manual a leads\n- Creación de campañas de seguimiento\n- Gestión manual de contactos")
