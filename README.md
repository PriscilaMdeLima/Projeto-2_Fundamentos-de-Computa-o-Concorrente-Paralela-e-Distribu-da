# Projeto 2 da Disciplina: Fundamentos de Computação Concorrente, Paralela e Distribuída.
Prof: Jorge Soares de Farias Júnior

Aluna: Priscila Maciel de Lima

Turma: ASD20252_4A


# Projeto de Microsserviços: Coleção de Desafios de Arquitetura

Este repositório contém uma coleção de projetos de exemplo, estruturados como "desafios", focados na exploração de conceitos e padrões de **microsserviços** e **conteinerização** utilizando Docker e Docker Compose.



## 🚀 Estrutura do Projeto

O projeto está organizado em cinco diretórios principais, cada um representando um desafio arquitetural distinto:

| Diretório | Foco Principal | Descrição Aparente |
| :--- | :--- | :--- |
| `desafio1` | Comunicação Cliente-Servidor | Implementação básica de um serviço e um cliente em Python, conteinerizados separadamente. |
| `desafio2` | Orquestração Simples | Configuração de um ambiente com Docker Compose para um ou mais serviços. |
| `desafio3` | Aplicação Conteinerizada | Desenvolvimento de uma aplicação Python (com `requirements.txt`) pronta para ser conteinerizada via `Dockerfile`. |
| `desafio4` | Interação entre Serviços | Estrutura para demonstrar a comunicação entre dois microsserviços (`service_a` e `service_b`). |
| `desafio5` | Arquitetura Completa | Simulação de uma arquitetura de microsserviços mais complexa, incluindo um **API Gateway** e serviços de domínio (`ms_users`, `ms_orders`). |

## 🧩 Detalhes dos Módulos (Desafios)

### Desafio 1: Comunicação Cliente-Servidor

Este módulo parece focado na configuração de um sistema básico de comunicação.

*   **Arquivos Chave:** `server.py`, `client.sh`, `Dockerfile.server`, `Dockerfile.client`, `docker-compose.yml`.
*   **Conceitos:** Conteinerização de componentes distintos (cliente e servidor), definição de serviços no Docker Compose.

### Desafio 2: Orquestração Simples

Este módulo é um *boilerplate* para iniciar um ambiente multi-container.

*   **Arquivos Chave:** `docker-compose.yml`.
*   **Conceitos:** Uso do Docker Compose para definir e executar aplicações multi-container.

### Desafio 3: Aplicação Conteinerizada

O foco aqui é a preparação de uma aplicação para o ambiente Docker.

*   **Arquivos Chave:** `app.py`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`.
*   **Conceitos:** Gerenciamento de dependências (`requirements.txt`), criação de imagem Docker otimizada (`Dockerfile`), e orquestração da aplicação.

### Desafio 4: Interação entre Serviços

Este desafio simula um cenário onde diferentes serviços precisam interagir.

*   **Estrutura:** Contém diretórios para `service_a` e `service_b`.
*   **Conceitos:** Descoberta de serviços, comunicação síncrona/assíncrona entre microsserviços.

### Desafio 5: Arquitetura de Microsserviços Completa

Representa a estrutura mais complexa, típica de um sistema real de e-commerce ou similar.

*   **Estrutura:** Contém diretórios para `gateway`, `ms_users` (microsserviço de usuários) e `ms_orders` (microsserviço de pedidos).
*   **Conceitos:** Padrão API Gateway, separação de responsabilidades por domínio (DDD), orquestração de múltiplos microsserviços.

## 🛠️ Como Executar (Instruções Genéricas)

Para executar qualquer um dos desafios que utilizam Docker Compose, você precisará ter o **Docker** e o **Docker Compose** instalados em sua máquina.

1.  **Navegue até o diretório do desafio desejado:**
    \`\`\`bash
    cd projeto-microsservicos/desafioX
    \`\`\`
    (Substitua `desafioX` por `desafio1`, `desafio2`, etc.)

2.  **Construa e Inicie os Serviços:**
    Execute o comando `docker-compose up` com a flag `-d` para rodar em *background*.

    \`\`\`bash
    docker-compose up --build -d
    \`\`\`

3.  **Verifique o Status:**
    Confirme se os containers estão rodando.

    \`\`\`bash
    docker-compose ps
    \`\`\`

4.  **Parar e Remover os Containers:**
    Para encerrar o ambiente.

    \`\`\`bash
    docker-compose down
    \`\`\`




