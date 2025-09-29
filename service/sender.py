import requests
import json

class ChatLLMSender:
    def __init__(self):
        self.url = "https://routellm.abacus.ai/v1/chat/completions"
        api_key = "s2_f9598089c8f9478fb4286dab1b68fe76"
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        self.stream = False # or False
      
    def send_request(self, prompt, history = []):
        message = {
            "role": "user",
            "content": prompt
        }
        history.append(message)
        payload = {
            "model": "route-llm",
            "messages": history,
            "stream": self.stream
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        response = response.json()
        message = response['choices'][0]['message']
        history.append(message)
        return history