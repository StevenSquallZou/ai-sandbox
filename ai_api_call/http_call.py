import requests
import json
import os


url = "https://api.deepseek.com/chat/completions"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + os.environ["deepseek_api_key"],
}

payload = json.dumps({
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"}
    ]
})

response = requests.request("POST", url, headers=headers, data=payload)
print(f"AI response: \n{response.text}")
