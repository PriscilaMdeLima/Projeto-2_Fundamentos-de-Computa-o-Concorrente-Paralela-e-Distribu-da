import os
import time
from sqlalchemy import create_engine, text, inspect

# Configuração do banco de dados
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost:5432/persisted_data")
TABLE_NAME = "data_entries"

def wait_for_db(engine):
    """Espera o banco de dados estar pronto."""
    print("Aguardando o banco de dados...")
    for i in range(10):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Banco de dados pronto!")
            return
        except Exception as e:
            print(f"Tentativa {i+1}/10 falhou: {e}")
            time.sleep(3)
    raise ConnectionError("Não foi possível conectar ao banco de dados.")

def setup_database(engine):
    """Cria a tabela se ela não existir."""
    inspector = inspect(engine)
    if not inspector.has_table(TABLE_NAME):
        print(f"Criando a tabela '{TABLE_NAME}'...")
        with engine.connect() as connection:
            connection.execute(text(f"""
                CREATE TABLE {TABLE_NAME} (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
                    message VARCHAR(255)
                );
            """))
            connection.commit()
        print(f"Tabela '{TABLE_NAME}' criada com sucesso.")
    else:
        print(f"Tabela '{TABLE_NAME}' já existe.")

def insert_data(engine, message):
    """Insere um novo registro na tabela."""
    print(f"Inserindo dados: '{message}'")
    with engine.connect() as connection:
        result = connection.execute(text(f"""
            INSERT INTO {TABLE_NAME} (message) VALUES (:message) RETURNING id;
        """), {"message": message})
        connection.commit()
        inserted_id = result.scalar_one()
    print(f"Dados inseridos com ID: {inserted_id}")
    return inserted_id

def read_data(engine):
    """Lê todos os registros da tabela."""
    print(f"Lendo todos os dados da tabela '{TABLE_NAME}'...")
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, timestamp, message FROM {TABLE_NAME} ORDER BY id;"))
        rows = result.fetchall()
    
    if not rows:
        print("Nenhum dado encontrado.")
        return []

    print(f"--- {len(rows)} Registro(s) Encontrado(s) ---")
    for row in rows:
        print(f"ID: {row[0]}, Timestamp: {row[1]}, Mensagem: {row[2]}")
    print("--------------------------------------")
    return rows

def main():
    """Função principal da aplicação."""
    print("Iniciando a aplicação de persistência de dados.")
    
    try:
        engine = create_engine(DATABASE_URL)
        
        # 1. Esperar e configurar o banco de dados
        wait_for_db(engine)
        setup_database(engine)
        
        # 2. Ler dados existentes (para mostrar a persistência)
        existing_data = read_data(engine)
        
        # 3. Inserir um novo dado
        new_message = f"Entrada de dados do container em {time.strftime('%Y-%m-%d %H:%M:%S UTC')}"
        insert_data(engine, new_message)
        
        # 4. Ler novamente para confirmar a nova inserção
        print("\n--- Leitura após a nova inserção ---")
        read_data(engine)
        
        print("\nDemonstração concluída. O container irá sair em 10 segundos.")
        print("Os dados foram salvos no volume 'postgres_data'.")
        time.sleep(10)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        # Manter o container rodando em caso de erro para inspeção
        time.sleep(3600)

if __name__ == "__main__":
    main()
