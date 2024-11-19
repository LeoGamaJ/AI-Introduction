Gemini Chat CLI

📝 Description

A simple Python script to interact with the Google Gemini API through a command-line interface (CLI). This project allows you to send prompts and receive responses from the Gemini language model directly in your terminal.

🚀 Features

Interactive chat with Gemini model
Secure API key loading via .env file
Error handling for different request scenarios
Easy chat termination by typing 'exit'

📋 Prerequisites

Python 3.7+
Google Cloud account with Gemini API access

🔧 Installation
1. Clone Repository
bashCopygit clone https://github.com/your-username/gemini-chat-cli.git
cd gemini-chat-cli
2. Set Up Virtual Environment (Optional but Recommended)
bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bashCopypip install -r requirements.txt
🔑 Configuration

Create a .env file in the project root
Add your Gemini API key:

CopyGEMINI_API_KEY=your_api_key_here
🖥️ Usage
bashCopypython gemini_chat.py
🛠️ Dependencies

os
requests
python-dotenv

🔒 Security

API key loaded from .env file
Error handling for various authentication scenarios

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to modify.
📜 License
[Choose a license, e.g., MIT]

📞 Contact
Developer: Leo Gama
Email: leo@leogama.cloud

For any issues, open a GitHub issue.
