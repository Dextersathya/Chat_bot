import requests
import json

API_KEY = "pxZviIyD.QkIx3uYh9Q8vmzn0JBJ85jo3p12ysCu8"
channel_token = "hello"  # Replace this with the actual channel token
url = f"https://payload.vextapp.com/hook/30C6E7ZL81/catch/{channel_token}"
headers = {
    "Content-Type": "application/json",
    "apikey": f"api-key {API_KEY}"
}
data = {
    "payload": "what is artificial intelligence"
}

response = requests.post(url, headers=headers, json=data)
response_data = response.json()

# Extract and print only the text from the response
print(response_data["text"])
