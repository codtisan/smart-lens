from app.bases.translator import TranslatorBase
import ollama

class OllamaChat(TranslatorBase):

    def __init__(self, model_name: str = "gemma2:2b") -> None:
        super().__init__()
        self.model = model_name

    async def translate(self, source_text: str, target_lang: str) -> str:
        prompt = f"Translate the following text to {target_lang}. Your answer should only contain the translated text: {source_text}"
        response = ollama.chat(
            model=self.model,
            messages=[
                  {
                    'role': 'user',
                    'content': prompt,
                  },
            ]
        )
        summarized_text = response["message"]["content"]
        return summarized_text