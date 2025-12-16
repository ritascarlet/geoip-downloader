FROM python:3.12-slim

WORKDIR /app

RUN pip install requests

COPY downloader.py /app/downloader.py

CMD ["python", "/app/downloader.py"]
