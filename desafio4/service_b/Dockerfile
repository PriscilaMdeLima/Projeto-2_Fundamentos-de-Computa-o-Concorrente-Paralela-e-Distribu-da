FROM python:3.11-slim

WORKDIR /app

RUN pip install Flask requests

COPY service_b.py .

EXPOSE 5002

CMD ["python", "service_b.py"]
