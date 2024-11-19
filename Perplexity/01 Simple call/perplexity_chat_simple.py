import requests
import json

# Define your API key
API_KEY = 'YOUR_API_KEY'  # Replace with your Perplexity API key

# Perplexity API URL
url = 'https://api.perplexity.ai/chat/completions'  # Example endpoint (verify documentation)

# Define a valid model according to documentation
model = 'llama-3.1-sonar-small-128k-online'  # Adjust according to allowed model

# Request body
data = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": "Explain how the internet works."  # Example text
        }
    ]
}

# Headers for the request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Send POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    # If successful, display returned content
    result = response.json()
    print("Perplexity API Response:")
    print(json.dumps(result, indent=2))
else:
    # If an error occurs, display status and error message
    print(f"Error {response.status_code}: {response.text}")
