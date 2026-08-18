import streamlit as st

from rag import criar_banco_vetorial
from rag import buscar_procedimento
from agente import responder

st.set_page_config(
    page_title="Eu sou LogiIA Assistente Logístico",
    page_icon="🚚",
    layout="wide",
)

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container{
    padding-top:2rem;
}

.titulo{
    font-size:40px;
    font-weight:700;
    color:#0F62FE;
}

.subtitulo{
    color:#666666;
    font-size:18px;
}

.caixa{
    background:white;
    padding:20px;
    border-radius:12px;
    border:1px solid #E6E6E6;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Banco Vetorial
# -----------------------------

@st.cache_resource
def carregar_banco():
    return criar_banco_vetorial()

banco = carregar_banco()

# -----------------------------
# Cabeçalho
# -----------------------------

st.markdown(
    """
<div class="titulo">
🚚 Eu sou LogiIA Assistente Logístico
</div>

<div class="subtitulo">
Consulte procedimentos internos, transações e tire suas dúvidas de como usar o sistema.
Use como referência os procedimentos disponíveis no banco de dados para desenvolver suas habilidades e conhecimento sobre o sistema interno da empresa.
</div>

<br>
""",
unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/3082/3082037.png", width=80)

    st.title("Sistema")

    st.metric("Procedimentos", "25")

    st.metric("Banco Vetorial", "FAISS")

    st.metric("Modelo IA", "Gemini")

    st.divider()

    st.write("Exemplos de perguntas:")

    st.caption("""
• Como emitir uma NF?

• Como cancelar uma NF?

• Como cadastrar motorista?

• Como criar um pedido?
""")

# -----------------------------
# Histórico
# -----------------------------

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Entrada
# -----------------------------

pergunta = st.chat_input(
    "Digite sua dúvida..."
)

if pergunta:

    st.session_state.mensagens.append(
        {
            "role":"user",
            "content":pergunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.spinner("Consultando procedimentos..."):

        documentos = buscar_procedimento(
            banco,
            pergunta
        )

        resposta = responder(
            pergunta,
            documentos
        )

    st.session_state.mensagens.append(
        {
            "role":"assistant",
            "content":resposta
        }
    )

    with st.chat_message("assistant"):

        st.markdown(resposta)

    with st.sidebar:

        st.divider()

        st.subheader("Documentos encontrados")

        for doc in documentos:

            with st.expander("Documento"):

                st.text(doc.page_content)