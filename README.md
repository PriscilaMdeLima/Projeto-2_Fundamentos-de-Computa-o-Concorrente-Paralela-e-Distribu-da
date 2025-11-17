# Projeto 2 da Disciplina: Fundamentos de Computação Concorrente, Paralela e Distribuída.
Prof: Jorge Soares de Farias Júnior
Aluna: Priscila Maciel de Lima
Turma: ASD20252_4A


# Desafio 1: Comunicação entre Dois Containers Docker usando Rede Customizada

## 📌 Descrição Geral

Este projeto demonstra, de forma **simples e didática**, como criar **dois containers Docker** a partir de uma **única imagem**, que se comunicam através de uma **rede Docker customizada**:

* **Container Servidor (MODE=server):** expõe um servidor web Flask na porta **8080**.
* **Container Cliente (MODE=client):** realiza requisições HTTP periódicas ao servidor usando `curl`.

A arquitetura foi criada para ser **minimalista**, fácil de rodar e entender, ideal para estudos e demonstrações práticas.

---

# 🏗️ Arquitetura da Solução

## 🔹 Visão Geral

```
+----------------------+         +-----------------------+
|     CLIENTE          |  --->   |       SERVIDOR        |
|  (curl em loop)      |         |   (Flask porta 8080)   |
+----------------------+         +-----------------------+
           ^                          |
           |                          |
           +------ Docker Network -----+
```

## 🔹 Componentes

### **1. Imagem Docker única**

Contém tanto o servidor Python/Flask quanto o cliente curl.
O comportamento é definido pela variável de ambiente `MODE`.

### **2. Container Servidor**

* Baseado em Python 3.10-slim
* Executa `app.py`
* Expõe a porta 8080
* Recebe requisições do container cliente

### **3. Container Cliente**

* Executa o script `client.sh`
* Realiza requisições HTTP a cada 5 segundos
* Conecta no servidor usando o hostname Docker: `server`

### **4. Rede Docker Customizada**

* Tipo: `bridge`
* Permite comunicação direta pelo nome do container

---

# 🧩 Decisões Técnicas

* **Um único Dockerfile:** reduz complexidade e facilita manutenção.
* **MODE=server / MODE=client:** simples chaveamento via variável de ambiente.
* **Flask:** escolhido por ser leve e fácil de configurar.
* **Alpine + curl:** garantindo cliente mínimo e eficiente.
* **Rede Docker customizada:** evita problemas de DNS e isola o ambiente.

---

# ⚙️ Funcionamento Detalhado

## 🔸 Fluxo Completo

1. O usuário cria a imagem Docker única.
2. É criada uma rede Docker chamada `minha-rede`.
3. O container **servidor** sobe, escutando em `0.0.0.0:8080`.
4. O container **cliente** sobe configurado com `MODE=client`.
5. O cliente executa `curl http://server:8080` a cada 5 segundos.
6. Ambos os logs podem ser observados em tempo real.

## 🔸 Microsserviços

Apesar de simples, a arquitetura segue o princípio de microsserviços:

* Cada container tem responsabilidade única
* Comunicação por rede interna
* Independência entre cliente e servidor

---

# 📁 Estrutura do Repositório

```
projeto-simples/
│── Dockerfile
│── app.py
│── client.sh
│── README.md
```

---

# 🚀 Como Executar o Projeto

## 1️⃣ Baixe ou clone o repositório

```
git clone https://github.com/SEU_USUARIO/projeto-simples.git
cd projeto-simples
```

## 2️⃣ Crie a imagem Docker

```
docker build -t projeto-simples .
```

## 3️⃣ Crie a rede Docker customizada

```
docker network create minha-rede
```

## 4️⃣ Inicie o Servidor Flask

```
docker run -d \
  --name server \
  --network minha-rede \
  -p 8080:8080 \
  projeto-simples
```

## 5️⃣ Inicie o Cliente Curl

```
docker run -d \
  --name client \
  --network minha-rede \
  -e MODE=client \
  projeto-simples
```

---

# 🧪 Testando a Comunicação

### 🔹 Ver logs do servidor

```
docker logs -f server
```

Você verá requisições chegando.

### 🔹 Ver logs do cliente

```
docker logs -f client
```

Você verá respostas do servidor.

### 🔹 Testar pelo navegador

Acesse:

```
http://localhost:8080
```

---

# 📄 Conclusão

Este projeto demonstra:

* Comunicação entre containers Docker
* Rede customizada
* Microsserviços simples (cliente/servidor)
* Uso de um único Dockerfile para múltiplas funções

Ideal para estudos, entrevistas técnicas ou aulas de Docker.

---

# 📌 Autor

Projeto criado para demonstração e estudos – personalize como quiser.
