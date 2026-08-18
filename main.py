from rag import criar_banco_vetorial, buscar_procedimento
from agente import responder


print("Inicializando sistema...")

banco = criar_banco_vetorial()

print("Sistema pronto!")


pergunta = input("\nDigite sua pergunta: ")


documentos = buscar_procedimento(
    banco,
    pergunta
)


resposta = responder(
    pergunta,
    documentos
)


print("\nResposta:")
print(resposta)