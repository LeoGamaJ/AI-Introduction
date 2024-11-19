import os
from dotenv import load_dotenv
import requests
import json
from typing import List, Dict, Optional, Union
from datetime import datetime

class PerplexityChat:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('PERPLEXITY_API_KEY')
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY não encontrada no arquivo .env")
            
        self.url = 'https://api.perplexity.ai/chat/completions'
        self.conversation_history: List[Dict[str, str]] = []
        
        self.available_models = [
            'llama-3.1-sonar-small-128k-chat',
            'llama-3.1-sonar-large-128k-chat',
            'llama-3.1-sonar-small-128k-online',
            'llama-3.1-sonar-large-128k-online',
            'llama-3.1-sonar-huge-128k-online'
        ]
        
        # Configurações padrão
        self.current_config = {
            'model': 'llama-3.1-sonar-small-128k-online',
            'temperature': 0.2,
            'top_p': 0.9,
            'top_k': 0,
            'max_tokens': None,
            'presence_penalty': 0,
            'frequency_penalty': 1,
            'return_citations': True,
            'return_related_questions': False,
            'search_recency_filter': None,
            'language': 'pt-br'  # Adicionado configuração de idioma
        }

        # Mensagens do sistema para cada idioma
        self.system_messages = {
            'pt-br': "Você é um assistente prestativo. Responda sempre em português do Brasil de forma clara e natural.",
            'en': "You are a helpful assistant. Always respond in English in a clear and natural way."
        }

    def create_headers(self) -> Dict[str, str]:
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_request_body(self, messages: List[Dict[str, str]]) -> Dict:
        # Adiciona a mensagem do sistema no início da conversa
        system_message = {
            "role": "system",
            "content": self.system_messages[self.current_config['language']]
        }
        
        full_messages = [system_message] + messages

        body = {
            "model": self.current_config['model'],
            "messages": full_messages,
            "temperature": self.current_config['temperature'],
            "top_p": self.current_config['top_p'],
            "top_k": self.current_config['top_k'],
            "presence_penalty": self.current_config['presence_penalty'],
            "frequency_penalty": self.current_config['frequency_penalty'],
            "return_citations": self.current_config['return_citations'],
            "return_related_questions": self.current_config['return_related_questions']
        }

        if self.current_config['max_tokens'] is not None:
            body["max_tokens"] = self.current_config['max_tokens']
            
        if self.current_config['search_recency_filter']:
            body["search_recency_filter"] = self.current_config['search_recency_filter']

        return body

    def send_message(self, message: str) -> Dict:
        self.conversation_history.append({"role": "user", "content": message})
        
        try:
            response = requests.post(
                self.url,
                headers=self.create_headers(),
                data=json.dumps(self.create_request_body(self.conversation_history))
            )
            
            response.raise_for_status()
            result = response.json()
            
            assistant_message = result['choices'][0]['message']
            self.conversation_history.append(assistant_message)

            # Adapt the citations to include index and URL
            citations = []
            for idx, citation in enumerate(assistant_message.get('citations', []), start=1):
                # Assuming 'citation' contains the URL directly 
                # Adjust this according to the actual structure of 'citation'
                citations.append({"index": idx, "url": citation})

            return {
                'content': assistant_message.get('content', ''),
                'citations': citations
            }

        except requests.exceptions.RequestException as e:
            error_msg = "Erro na requisição" if self.current_config['language'] == 'pt-br' else "Request error"
            print(f"{error_msg}: {str(e)}")
            if hasattr(e.response, 'text'):
                response_msg = "Texto da resposta" if self.current_config['language'] == 'pt-br' else "Response text"
                print(f"{response_msg}: {e.response.text}")
            return {'error': str(e)}

    def save_conversation(self, filename: Optional[str] = None) -> None:
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'conversation_{timestamp}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
        
        save_msg = "Conversa salva em" if self.current_config['language'] == 'pt-br' else "Conversation saved to"
        print(f"{save_msg} {filename}")

    def clear_conversation(self) -> None:
        self.conversation_history = []
        clear_msg = "Histórico de conversa limpo" if self.current_config['language'] == 'pt-br' else "Conversation history cleared"
        print(clear_msg)

    def show_current_config(self):
        title = "\nConfigurações atuais:" if self.current_config['language'] == 'pt-br' else "\nCurrent settings:"
        print(title)
        for key, value in self.current_config.items():
            print(f"{key}: {value}")

    def configure_settings(self):
        is_ptbr = self.current_config['language'] == 'pt-br'
        
        print("\n=== " + ("Configuração do Chat" if is_ptbr else "Chat Configuration") + " ===")
        print("Pressione Enter para manter o valor atual" if is_ptbr else "Press Enter to keep current value")
        
        # Configuração de idioma
        print("\n" + ("Idiomas disponíveis:" if is_ptbr else "Available languages:"))
        print("1. Português (pt-br)\n2. English (en)")
        lang_choice = input("Escolha o idioma (1-2)" if is_ptbr else "Choose language (1-2): ")
        if lang_choice == '1':
            self.current_config['language'] = 'pt-br'
        elif lang_choice == '2':
            self.current_config['language'] = 'en'
        
        # Atualiza a variável is_ptbr após a possível mudança de idioma
        is_ptbr = self.current_config['language'] == 'pt-br'

        # Modelo
        print(f"\n" + ("Modelos disponíveis:" if is_ptbr else "Available models:"))
        for idx, model in enumerate(self.available_models, 1):
            print(f"{idx}. {model}")
        model_prompt = "Escolha o número do modelo" if is_ptbr else "Choose model number"
        model_choice = input(f"{model_prompt} (atual: {self.current_config['model']}): ")
        if model_choice.isdigit() and 1 <= int(model_choice) <= len(self.available_models):
            self.current_config['model'] = self.available_models[int(model_choice)-1]

        # Temperature
        temp_prompt = "Temperature (0-2)" if is_ptbr else "Temperature (0-2)"
        temp = input(f"{temp_prompt} (atual: {self.current_config['temperature']}): ")
        if temp:
            self.current_config['temperature'] = float(temp)

        # Top P
        top_p = input(f"Top P (0-1) (atual: {self.current_config['top_p']}): ")
        if top_p:
            self.current_config['top_p'] = float(top_p)

        # Max Tokens
        tokens_prompt = "Max Tokens" if is_ptbr else "Max Tokens"
        max_tokens = input(f"{tokens_prompt} (atual: {self.current_config['max_tokens']}): ")
        if max_tokens:
            self.current_config['max_tokens'] = int(max_tokens) if max_tokens.lower() != 'none' else None

        # Search Recency
        print("\n" + ("Opções de recência de busca:" if is_ptbr else "Search recency options:"))
        print("1. month\n2. week\n3. day\n4. hour\n5. none")
        recency_prompt = "Escolha a recência (1-5)" if is_ptbr else "Choose recency (1-5)"
        recency = input(f"{recency_prompt} (atual: {self.current_config['search_recency_filter']}): ")
        if recency:
            recency_options = {
                '1': 'month',
                '2': 'week',
                '3': 'day',
                '4': 'hour',
                '5': None
            }
            self.current_config['search_recency_filter'] = recency_options.get(recency)

        # Citations
        citations_prompt = "Retornar citações (true/false)" if is_ptbr else "Return citations (true/false)"
        citations = input(f"{citations_prompt} (atual: {self.current_config['return_citations']}): ")
        if citations.lower() in ['true', 'false']:
            self.current_config['return_citations'] = citations.lower() == 'true'

        print("\n" + ("Configurações atualizadas!" if is_ptbr else "Settings updated!"))
        self.show_current_config()

def main():
    try:
        chat = PerplexityChat()
        is_ptbr = chat.current_config['language'] == 'pt-br'
        
        print("\n=== Perplexity AI Chat ===")
        print("Comandos disponíveis:" if is_ptbr else "Available commands:")
        print("'config' - " + ("Configurar parâmetros do chat" if is_ptbr else "Configure chat parameters"))
        print("'settings' - " + ("Mostrar configurações atuais" if is_ptbr else "Show current settings"))
        print("'save' - " + ("Salvar conversa" if is_ptbr else "Save conversation"))
        print("'clear' - " + ("Limpar histórico" if is_ptbr else "Clear history"))
        print("'exit' - " + ("Sair" if is_ptbr else "Exit"))
        print("=" * 30)

        while True:
            is_ptbr = chat.current_config['language'] == 'pt-br'
            prompt = "\nVocê: " if is_ptbr else "\nYou: "
            user_input = input(prompt).strip()
            
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'save':
                chat.save_conversation()
                continue
            elif user_input.lower() == 'clear':
                chat.clear_conversation()
                continue
            elif user_input.lower() == 'config':
                chat.configure_settings()
                continue
            elif user_input.lower() == 'settings':
                chat.show_current_config()
                continue
            elif not user_input:
                continue

            response = chat.send_message(user_input)

            if 'error' in response:
                error_msg = "Erro" if is_ptbr else "Error"
                print(f"\n{error_msg}: {response['error']}")
                continue

            assistant_msg = "Assistente" if is_ptbr else "Assistant"
            print(f"\n{assistant_msg}:", response['content'])
            
            if response.get('citations'):
                citations_msg = "Citações" if is_ptbr else "Citations"
                print(f"\n{citations_msg}:")
                for citation in response['citations']:
                    print(f"- {citation}")

    except Exception as e:
        error_msg = "Erro ao iniciar o chat" if chat.current_config['language'] == 'pt-br' else "Error starting chat"
        print(f"{error_msg}: {str(e)}")

if __name__ == "__main__":
    main()