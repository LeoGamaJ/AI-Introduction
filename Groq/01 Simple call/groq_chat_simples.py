import os
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar a chave da API através da variável de ambiente
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Pedir input do usuário
user_input = input("Insira sua pergunta ou texto para completar: ")

# Realizar uma requisição de chat completion com o input do usuário
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="llama3-8b-8192",
)

# Exibir a resposta
print(chat_completion.choices[0].message.content)
