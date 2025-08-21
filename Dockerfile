FROM python:3.11-slim

WORKDIR /app



COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m nltk.downloader vader_lexicon

COPY . .

EXPOSE 8080

CMD ["python","/app/app/main.py"]