# AI Custom API Requests

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

Repositório de scripts para integração com diferentes APIs de IA, contendo implementações para:

## 📋 Descrição
Coleção de scripts Python para fazer requisições personalizadas em diversas APIs de inteligência artificial, incluindo:
- OpenAI (GPT-4, GPT-3.5)
- Google Gemini
- Anthropic Claude
- Groq
- Perplexity

## ✨ Funcionalidades
- Interface padrão para diferentes provedores de IA
- Configuração simplificada via arquivo .env
- Histórico automático de conversas
- Suporte a modelos mais recentes

## 🛠️ Instalação
```bash
git clone https://github.com/seu-usuario/ai-custom-api-requests.git
cd ai-custom-api-requests
pip install -r requirements.txt
```

## 🚀 Uso
1. Crie um arquivo `.env` com suas chaves de API:
```ini
OPENAI_API_KEY=suachave
ANTHROPIC_API_KEY=suachave
GEMINI_API_KEY=suachave
GROQ_API_KEY=suachave
PERPLEXITY_API_KEY=suachave
```

2. Execute o script desejado:
```bash
python openai_request.py
python gemini_req.py
python anthropic_request.py
python groq_requests.py
python perplexity_request.py
```

## 📂 Estrutura de Arquivos
```
.
├── .env.example
├── requirements.txt
├── openai_request.py       # Interface para OpenAI
├── gemini_req.py           # Integração com Google Gemini
├── anthropic_request.py    # Implementação Claude da Anthropic
├── groq_requests.py        # Requisições para Groq Cloud
├── perplexity_request.py   # Conexão com Perplexity API
└── historico/              # Registro de conversas
    ├── anthropic_chat_*.md
    ├── gemini_chat_*.md
    └── groq_chat_*.md
```

## 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:
1. Faça um Fork do projeto
2. Crie sua Branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença
Distribuído sob licença MIT.

## 👤 Author

Leo Gama
- GitHub: [@LeoGamaJ](https://github.com/LeoGamaJ)
- Email: leo@leogama.cloud 
- LinkedIn: (https://www.linkedin.com/in/leonardo-gama-jardim/)
.
