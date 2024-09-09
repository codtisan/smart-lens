from fastapi import FastAPI, UploadFile, File, Body
from datetime import datetime
from app.typings.api_response import HealthResponse, OCRResponse, OCRResult
from app.typings.translation import TranslationInfo
from app.libs.ocr.pytesseract import Pytesseract
from app.libs.translator.duckduckgo import DuckduckgoTranslator
import io

app = FastAPI()


@app.get("/")
async def get_health() -> HealthResponse:
    return HealthResponse(status="success", status_code=200, timestamp=datetime.now())

@app.post("/recognize")
async def get_text(image_file: UploadFile = File(...)) -> OCRResponse:
    ocr = Pytesseract(image=io.BytesIO(image_file.file.read()))
    text = await ocr.extract()
    return OCRResponse(
        status="success",
        status_code=201,
        timestamp=datetime.now(),
        result=OCRResult(
            text=text
        )
    )

@app.post("/translate")
async def get_translations(translation_info: TranslationInfo = Body(...), image_file: UploadFile = File(...)) -> OCRResponse:
    ocr = Pytesseract(image=io.BytesIO(image_file.file.read()))
    text = await ocr.extract()
    translator = DuckduckgoTranslator()
    translated_text = await translator.translate(source_text=text, target_lang=translation_info.target_lang)
    return OCRResponse(
        status="success",
        status_code=201,
        timestamp=datetime.now(),
        result=OCRResult(
            text=translated_text
        )
    )