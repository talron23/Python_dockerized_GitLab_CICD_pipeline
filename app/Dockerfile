FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY templates /app/templates

COPY . .

CMD ["python", "app.py"]