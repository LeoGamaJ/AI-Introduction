# Advanced Gemini CLI

## 📝 Description
An advanced Python CLI for interacting with Google Gemini, supporting multiple content types and dynamic configuration.

## 🚀 Features

### Basic Version (gemini_custom_call01.py)
- Interactive text chat with Gemini
- Dynamic configuration of model parameters
- Error handling for API requests
- Environment-based API key management

### Advanced Version (gemini_custom_call02.py)
- Support for multiple content types:
  - Text
  - Images
  - PDFs
  - HTML
  - Markdown
  - Code files
- Image processing with auto-resizing
- Syntax highlighting for code
- Advanced configuration management
- File content processing

## 📋 Prerequisites
- Python 3.8+
- Google Cloud account with Gemini API access

## 🔧 Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/gemini-advanced-cli.git
cd gemini-advanced-cli
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configuration
1. Create a `.env` file in the project root
2. Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 🖥️ Usage

### Basic Version
```bash
python gemini_basic.py
```

### Advanced Version
```bash
python gemini_advanced.py
```

### Available Commands
- `config`: Modify model parameters
- `arquivo`: Upload and analyze files
- `sair`: Exit the chat

## 🛠️ Dependencies
- `requests`
- `python-dotenv`
- `Pillow`
- `markdown`
- `beautifulsoup4`
- `pygments`
- `PyMuPDF` (optional, for PDF support)

## 🔒 Security
- API key loaded from `.env`
- Comprehensive error handling
- Secure file processing

## 🤝 Contributing
Contributions welcome! Please open an issue first to discuss proposed changes.

## 📜 License
MIT

## 📞 Contact
- Developer: Leo Gama
- Email: leo@leogama.cloud
  
For issues, open a GitHub issue.

## 🔮 Future Improvements
- Persistent chat history
- Multi-turn conversations
- Enhanced file type support
