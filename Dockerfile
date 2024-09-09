FROM python:3.12-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    tesseract-ocr

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "python3", "main.py" ]