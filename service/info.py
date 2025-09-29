from store.clients import clients
from store.conversations import conversations
from service.sender import ChatLLMSender
from store.prompts import chatbot

class InfoService:
    def __init__(self, client, conversation):
        self.sender = ChatLLMSender()
        self.client = client.lower()
        self.conversation_id = conversation
        try:
            self.client_prompt = clients[self.client]
        except KeyError:
            return "Error"
        if conversation not in conversations:
            prompt = chatbot.format(company= self.client) + self.client_prompt
            conversations[conversation] = [{"role": "user", "content": prompt}]
        self.history = conversations[self.conversation_id] 

    
    def handle_conversation(self, message):
        self.hisotry = self.sender.send_request(message, self.hisotry)
        conversations[self.conversation] = self.history
        return conversations[self.conversation][-1]["content"]