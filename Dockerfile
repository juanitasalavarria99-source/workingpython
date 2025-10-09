FROM python:3.9-slim

WORKDIR /app

COPY v2_oop/bank.py .

CMD ["python", "bank.py"]
