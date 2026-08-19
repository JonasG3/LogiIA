# LogiIA
LogiIA é um agente de IA desenvolvido para auxiliar colaboradores na utilização dos sistemas internos da empresa, fornecendo orientações sobre procedimentos, transações, cadastros, emissão de documentos, notas fiscais e demais operações do dia a dia.

link: https://logibott.streamlit.app

Video e fotos de evidencia do projeto rodando dentro de assets

# LogiIA
LogiIA é um agente de IA desenvolvido para auxiliar colaboradores na utilização dos sistemas internos da empresa, fornecendo orientações sobre procedimentos, transações, cadastros, emissão de documentos, notas fiscais e demais operações do dia a dia.

O projeto combina busca semântica com geração de respostas por IA, permitindo consultar procedimentos internos de forma rápida e contextualizada.

# Visão geral
O sistema utiliza Retrieval Augmented Generation (RAG) para:

carregar procedimentos armazenados em arquivo CSV
transformar esses dados em embeddings
buscar os trechos mais relevantes para a pergunta do usuário
enviar o contexto ao modelo de linguagem para responder com base somente nos procedimentos disponíveis
Isso torna o assistente útil para dúvidas operacionais de logística, como:

emissão de Nota Fiscal
cancelamento de NF
cadastro de clientes
cadastro de produtos
cadastro de motoristas
criação de pedidos
consulta de procedimentos internos
explicações de transações e rotinas do sistema


# Stack tecnológica
A stack principal do projeto inclui:

Python 3.12
Streamlit — interface web para interação com o usuário
LangChain — orquestração do fluxo de RAG
LangChain Community — carregamento de dados e integrações auxiliares
LangChain Google GenAI — integração com modelos Gemini
FAISS — banco vetorial para busca por similaridade
Google Generative AI Embeddings — geração de embeddings
python-dotenv — carregamento de variáveis de ambiente
CSVLoader — leitura do arquivo com os procedimentos
Google Gemini — modelo de geração de respostas


# Arquitetura do projeto
O fluxo do sistema funciona da seguinte forma:

Os procedimentos são armazenados em um arquivo CSV.
O módulo de RAG carrega esses registros.
Os textos são convertidos em embeddings.
A busca por similaridade identifica os documentos mais relevantes.
O modelo de linguagem recebe esse contexto e responde de forma estruturada.
A interface do usuário consulta o sistema em tempo real.


# Estrutura de arquivos
app.py — aplicação principal em Streamlit
agente.py — lógica do agente IA e prompt do assistente
rag.py — criação do banco vetorial e busca por similaridade
main.py — execução do sistema em modo terminal
procedimentos_sistema_logistica_ficticio.csv — base de conhecimento com procedimentos
requirements.txt — dependências do projeto
.env — variável de ambiente com a chave da API do Google AI
runtime.txt — versão do Python utilizada


# Como funciona a busca e a resposta
O fluxo principal é:

O usuário faz uma pergunta.
O sistema busca os procedimentos mais similares no banco vetorial FAISS.
Os documentos recuperados são passados como contexto para o modelo Gemini.
O modelo responde somente com base no contexto encontrado.
Se o conteúdo não existir, a IA deve informar que a informação não foi encontrada.


# Observações
O projeto foi construído como prova de conceito de agente com RAG para suporte interno logístico.
A resposta do assistente é orientada por contexto, evitando inventar regras ou procedimentos inexistentes.
O arquivo CSV funciona como base de conhecimento e pode ser expandido com novos procedimentos da operação.
