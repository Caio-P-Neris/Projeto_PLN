import streamlit as st
from sentmarket import chatbot_news  # importe sua função

st.set_page_config(page_title="Chatbot Financeiro", page_icon="💬")

st.title("💬 Chatbot de Notícias Financeiras")

# guarda mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# exibe mensagens antigas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input do usuário
if pergunta := st.chat_input("Digite sua pergunta..."):

    # adiciona pergunta ao histórico
    st.session_state.messages.append({"role": "user", "content": pergunta})

    # exibe
    with st.chat_message("user"):
        st.markdown(pergunta)

    # resposta do chatbot
    with st.chat_message("assistant"):
        resposta = chatbot_news(pergunta)   # mude para aceitar parâmetro
        st.write(resposta)

    # salva resposta
    st.session_state.messages.append({"role": "assistant", "content": resposta})
