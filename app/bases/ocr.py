from abc import abstractmethod, ABC

class OpticalCharacterRecognizerBase(ABC):

    @abstractmethod
    async def extract() -> str:
        pass