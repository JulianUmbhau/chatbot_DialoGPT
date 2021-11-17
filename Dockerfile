FROM python:3.8.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

EXPOSE 8080

CMD ["python3", "app.py", "serve"]