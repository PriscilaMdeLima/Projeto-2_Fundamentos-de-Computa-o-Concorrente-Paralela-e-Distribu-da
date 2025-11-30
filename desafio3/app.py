from flask import Flask, jsonify
import redis
import psycopg2
import os
import time

app = Flask(__name__)

# Configurações do PostgreSQL
DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "app_db")
DB_USER = os.environ.get("DB_USER", "user")
DB_PASS = os.environ.get("DB_PASS", "password")

# Configurações do Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "cache")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

# Conexão com Redis
cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_db_connection():
    """Tenta conectar ao PostgreSQL."""
    conn = None
    max_retries = 5
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
            return conn
        except psycopg2.OperationalError as e:
            print(f"Tentativa {i+1}/{max_retries} de conexão ao DB falhou: {e}")
            time.sleep(2)
    raise ConnectionError("Não foi possível conectar ao banco de dados após várias tentativas.")

def initialize_db():
    """Cria a tabela se não existir."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS access_count (
                id SERIAL PRIMARY KEY,
                count INTEGER DEFAULT 0
            );
        """)
        conn.commit()
        # Garante que haja um registro para atualizar
        cur.execute("SELECT count FROM access_count WHERE id = 1;")
        if cur.fetchone() is None:
            cur.execute("INSERT INTO access_count (id, count) VALUES (1, 0);")
            conn.commit()
        cur.close()
        conn.close()
        print("Banco de dados inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

@app.before_request
def check_services():
    """Verifica a conexão com os serviços antes de cada requisição."""
    try:
        # Verifica Redis
        cache.ping()
    except Exception:
        print("Erro de conexão com Redis.")
        # Não interrompe a requisição, apenas registra o erro
    
    try:
        # Verifica DB
        get_db_connection().close()
    except Exception:
        print("Erro de conexão com PostgreSQL.")
        # Não interrompe a requisição, apenas registra o erro

@app.route('/')
def index():
    # 1. Acessa o Cache (Redis)
    try:
        hits = cache.incr('hits')
    except Exception:
        hits = "Cache Indisponível"

    # 2. Acessa o Banco de Dados (PostgreSQL)
    db_status = "OK"
    db_count = 0
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Atualiza o contador no DB
        cur.execute("UPDATE access_count SET count = count + 1 WHERE id = 1 RETURNING count;")
        db_count = cur.fetchone()[0]
        conn.commit()
        
        cur.close()
        conn.close()
    except Exception as e:
        db_status = f"Erro: {e}"

    return jsonify({
        "message": "Aplicação orquestrada com Docker Compose",
        "services": {
            "web": "Flask (Python)",
            "database": f"PostgreSQL - Status: {db_status}",
            "cache": f"Redis - Status: {'OK' if isinstance(hits, int) else hits}"
        },
        "counters": {
            "redis_hits": hits,
            "db_access_count": db_count
        }
    })

if __name__ == '__main__':
    # Inicializa o DB antes de rodar a aplicação
    initialize_db()
    app.run(host='0.0.0.0', port=5000)
