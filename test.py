import streamlit as st
from service.info import InfoService
from uuid import uuid4

# Configuración de la página
st.set_page_config(
    page_title="Demo Chatbot - Tu Negocio",
    page_icon="🤖",
    layout="wide"
)

# Sidebar para configurar el negocio
st.sidebar.header("⚙️ Configuración del Negocio")
business_name = st.sidebar.text_input("Nombre del negocio:", "BigDogs")

# Título principal
st.title(f"🤖 Chatbot Demo - {business_name}")
conversation_number = str(uuid4())
info = InfoService(business_name, conversation_number)

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensaje de bienvenida automático
    welcome_msg = f"¡Hola! 👋 Soy el asistente virtual de {business_name}. ¿En qué puedo ayudarte hoy?"
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

# Mostrar historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Mostrar mensaje del usuario
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                
                
                
                response = info.handle_conversation(prompt)
                
                if response:
                    bot_response = response
                else:
                    bot_response = "Lo siento, hubo un problema. Por favor intenta de nuevo."
                
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
                
            except Exception as e:
                error_msg = "Disculpa, estoy teniendo problemas técnicos. Por favor intenta más tarde."
                st.markdown(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Botón para limpiar chat
if st.sidebar.button("🗑️ Limpiar conversación"):
    st.session_state.messages = []
    st.rerun()

# Información adicional en sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Demo Info")
st.sidebar.info(f"Este es un demo de chatbot personalizado para {business_name}. Cambia la configuración arriba para ver cómo se adapta a diferentes negocios.")