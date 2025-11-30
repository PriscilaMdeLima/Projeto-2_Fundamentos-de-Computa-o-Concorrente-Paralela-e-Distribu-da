# Use uma imagem base Python leve
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script da aplicação
COPY app.py .

# Comando para rodar a aplicação
CMD ["python", "app.py"]
