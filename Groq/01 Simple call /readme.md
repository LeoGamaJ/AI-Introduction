# Groq Chat Client

A simple Python client to interact with the Groq API using the LLaMA3 model.

## 📋 Description

This project implements a chat client that uses the Groq API to generate responses based on user input. The script uses the LLaMA3-8B-8192 model to process and respond to user inputs.

## 🚀 Features

- Simple command-line interface
- Groq API integration
- Secure environment variable configuration
- Uses LLaMA3-8B-8192 model

## 📦 Prerequisites

- Python 3.6+
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/groq-chat-client.git
cd groq-chat-client
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Create a `.env` file in the project root
   - Add your Groq API key:
```bash
GROQ_API_KEY=your-api-key-here
```

## 💻 How to Use

1. Run the script:
```bash
python chat_client.py
```

2. Type your question or text when prompted
3. Wait for the model's response

## 📄 Usage Example

```python
Enter your question or text to complete: What is the capital of Brazil?
# The model will process your question and return a response
```

## 📝 Requirements.txt
```
groq==0.4.0
python-dotenv==1.0.0
```

## 🔐 Security

- Never share your API key
- Always use environment variables for credentials
- Keep the `.env` file in `.gitignore`

## ⚠️ Important Notes

- The model may have input size limitations
- Responses may vary depending on context
- Check Groq documentation for usage limits

## 🤝 Contributing

1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

Your Name
- GitHub: [@LeoGamaJ](https://github.com/LeoGamaJ)
- Email: leo@leogama.cloud or open an issue on GitHub.
