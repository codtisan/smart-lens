from abc import abstractmethod, ABC

class TranslatorBase(ABC):

    @abstractmethod
    async def translate(source_text: str) -> str:
        pass