FROM python:3.8.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

ENV dash_port=80
ENV dash_debug="False"

CMD ["python3", "app.py"]