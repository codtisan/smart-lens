from app.server import app
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()


def bootstrap() -> None:
    port = int(os.getenv("PORT"))
    uvicorn.run(app=app, port=port, host="0.0.0.0")

bootstrap()
