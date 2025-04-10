import openai

class OpenAIClient:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def chat(self, prompt: str, system_message: str = "You are a helpful assistant.") -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Erreur lors de l'appel à l'API : {e}"

# Utilisation
if __name__ == "__main__":
    api_key = "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"
    client = OpenAIClient(api_key)

    question = "Explique-moi la théorie de la relativité en termes simples."
    réponse = client.chat(question)
    print("Réponse de l'IA :", réponse)
