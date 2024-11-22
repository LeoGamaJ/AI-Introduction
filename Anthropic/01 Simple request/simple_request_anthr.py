import requests
import os

# Configuração da API
API_KEY = "<YOUR_API_KEY>"
API_URL = "https://api.anthropic.com/v1/messages"

# Configure sua chave API como uma variável de ambiente por segurança
os.environ["ANTHROPIC_API_KEY"] = API_KEY

# Função para enviar uma mensagem para o Claude 3.5
def enviar_mensagem_claude(mensagem):
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01"
    }

    data = {
        "model": "claude-3.5-sonnet",
        "messages": [{"role": "user", "content": mensagem}],
        "max_tokens": 1000
    }

    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["content"][0]["text"]
    else:
        return f"Erro: {response.status_code} - {response.text}"

# Exemplo de uso
if __name__ == "__main__":
    mensagem_usuario = "Olá, Claude! Pode me dar um resumo sobre inteligência artificial?"
    resposta = enviar_mensagem_claude(mensagem_usuario)
    print(resposta)
