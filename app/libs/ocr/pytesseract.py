from app.bases.ocr import OpticalCharacterRecognizerBase
import pytesseract
from PIL import Image

class Pytesseract(OpticalCharacterRecognizerBase):
    def __init__(self, image: str | bytes) -> None:
        super().__init__()
        self.image = Image.open(image)

    async def extract(self) -> str:
        text = pytesseract.image_to_string(self.image)
        return text