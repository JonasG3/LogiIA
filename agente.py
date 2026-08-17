import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


def responder(pergunta, documentos):

    contexto = "\n\n".join(
        documento.page_content
        for documento in documentos
    )

    prompt = f"""
Você é um assistente especializado nos procedimentos
internos de uma empresa de logística.

Sua função é ajudar colaboradores a utilizar o sistema interno.

Utilize SOMENTE as informações presentes no CONTEXTO.

Se a resposta não estiver no contexto, diga:

"Não encontrei essa informação nos procedimentos disponíveis."

Não invente:
- nomes de transações;
- códigos;
- etapas;
- regras;
- informações que não estejam no contexto.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

Responda de forma clara, objetiva e organizada.
"""

    resposta = llm.invoke(prompt)

    if isinstance(resposta.content, list):
        return "".join(
            item["text"]
            for item in resposta.content
            if item.get("type") == "text"
        )

    return resposta.content