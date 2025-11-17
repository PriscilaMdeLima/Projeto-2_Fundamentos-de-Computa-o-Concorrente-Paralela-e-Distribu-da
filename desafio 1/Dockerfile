FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY app.py .
COPY client.sh .
RUN chmod +x client.sh

RUN pip install flask

ENV MODE=server

CMD ["/bin/sh", "-c", "if [ \"$MODE\" = \"server\" ]; then python app.py; else sh client.sh; fi"]
