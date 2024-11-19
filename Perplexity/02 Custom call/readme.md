# Perplexity_Chat CLI

An interactive command-line interface for the Perplexity AI API, enabling conversations in Portuguese and English with advanced AI models.

## 🌟 Features
- 🌍 Bilingual support (Portuguese-BR and English)
- ⚙️ Interactive parameter configuration
- 💾 Conversation saving
- 📚 Citation support
- 🔄 Conversation history
- 🔐 Secure credential management via .env file

## 📋 Requirements
- Python 3.7+
- Perplexity AI API Key

## 🛠️ Installation
1. Clone the repository:
```bash
git clone [repository-url]
cd [directory-name]
```

2. Install dependencies:
```bash
pip install python-dotenv requests
```

3. Create a `.env` file in the project root:
```env
PERPLEXITY_API_KEY=your-api-key-here
```

## ⚙️ Available Models
- llama-3.1-sonar-small-128k-chat
- llama-3.1-sonar-large-128k-chat
- llama-3.1-sonar-small-128k-online
- llama-3.1-sonar-large-128k-online
- llama-3.1-sonar-huge-128k-online

## 🚀 Usage
Run the script:
```bash
python script.py
```

### Available Commands
- `config` - Opens configuration menu
- `settings` - Shows current settings
- `save` - Saves current conversation
- `clear` - Clears conversation history
- `exit` - Closes the program

### Configurable Parameters
- **Language**: Portuguese-BR or English
- **Model**: Choose from available models
- **Temperature**: Controls response creativity (0-2)
- **Top P**: Controls text diversity (0-1)
- **Max Tokens**: Maximum response token limit
- **Search Recency**: Time filter for searches (month/week/day/hour)
- **Citations**: Enable/disable response citations

## 🔧 Interactive Configuration
The `config` command allows adjusting:
1. Interaction language
2. AI model
3. Text generation parameters
4. Search filters
5. Citation settings

## 📝 Usage Example
```python
# Starting a conversation
You: What is the capital of Brazil?
Assistant: The capital of Brazil is Brasília, located in the Federal District. It was inaugurated on April 21, 1960, replacing Rio de Janeiro as the federal capital.

# Changing settings
You: config
[Configuration menu appears]

# Saving the conversation
You: save
Conversation saved to conversation_20241114_123456.json
```

## 💾 Saving Format
Conversations are saved in JSON format with:
- Timestamp
- Complete message history
- Conversation metadata

## ⚠️ Important Notes
1. Keep your API key secure
2. Check API usage limits
3. Citations only work with online models
4. Some settings may not be available on all models

## 🤝 Contributing
Contributions are welcome! Please feel free to:
1. Report bugs
2. Suggest improvements
3. Submit pull requests

## 📜 License
This project is licensed under the MIT License

## 📞 Support
For support:
1. Open an issue
2. Contact via [leo@leogama.cloud]
3. Consult the API documentation

---
⚡ Developed by Leo Gama
