FROM python:3.11-slim

WORKDIR /app

RUN pip install Flask

COPY service_a.py .

EXPOSE 5001

CMD ["python", "service_a.py"]
