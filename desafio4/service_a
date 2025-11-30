from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice", "status": "ativo", "member_since": "2023-01-15"},
    {"id": 2, "name": "Bob", "status": "inativo", "member_since": "2022-11-01"},
    {"id": 3, "name": "Charlie", "status": "ativo", "member_since": "2024-05-20"},
]

@app.route('/users')
def get_users():
    print("Microsserviço A: Retornando lista de usuários.")
    return jsonify(USERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
