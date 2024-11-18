FROM python:3.12

WORKDIR /app

COPY main.py .
COPY my_email.py .
COPY correo.py .
COPY index.html .
COPY requirements.txt .
COPY static static

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]