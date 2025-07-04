import openai
from config import OPENAI_API_KEY, MODEL

openai.api_key = OPENAI_API_KEY

class PromptEngine:
    def __init__(self, system_message="Você é Alice IA, uma assistente inteligente e criativa."):
        self.system_message = system_message

    def generate_response(self, user_input):
        try:
            response = openai.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": user_input},
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Erro ao gerar resposta: {e}"