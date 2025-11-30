from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# O nome do host é o nome do serviço no docker-compose
SERVICE_A_URL = os.environ.get("SERVICE_A_URL", "http://service_a:5001/users")

@app.route('/combined_info')
def get_combined_info():
    print("Microsserviço B: Iniciando requisição para o Microsserviço A.")
    
    try:
        # Faz a requisição HTTP para o Microsserviço A
        response = requests.get(SERVICE_A_URL)
        response.raise_for_status() # Levanta exceção para códigos de erro HTTP
        users = response.json()
        
        combined_data = []
        for user in users:
            status_text = "ativo" if user.get("status") == "ativo" else "inativo"
            combined_data.append(
                f"Usuário {user.get('name')} ({user.get('id')}) está {status_text} desde {user.get('member_since')}."
            )
            
        print("Microsserviço B: Dados combinados com sucesso.")
        return jsonify({
            "status": "success",
            "source_service": "Microsserviço A",
            "combined_info": combined_data
        })
        
    except requests.exceptions.RequestException as e:
        print(f"Microsserviço B: Erro ao conectar ao Microsserviço A: {e}")
        return jsonify({
            "status": "error",
            "message": f"Não foi possível obter dados do Microsserviço A. Erro: {e}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
