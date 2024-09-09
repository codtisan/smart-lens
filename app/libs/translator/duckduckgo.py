from duckduckgo_search import DDGS
from app.bases.translator import TranslatorBase



class DuckduckgoTranslator(TranslatorBase):
    def __init__(self) -> None:
        super().__init__()
        self.ddgs = DDGS()
    
    async def translate(self, source_text: str, target_lang: str) -> str:
        translated_text = self.ddgs.chat(f"Translate the following text to {target_lang}. Your answer should only contain the translated text: {source_text}")
        return translated_text