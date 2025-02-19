import ollama

class ChatService:
    def __init__(self, model_name="deepseek-r1:1.5b"):
        self.model_name = model_name

    def generate_response(self, user_input):
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": user_input}])
        return response['message']['content']
