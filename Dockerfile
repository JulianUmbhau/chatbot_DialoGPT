FROM python:3.8.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

CMD ["python3", "app.py"]