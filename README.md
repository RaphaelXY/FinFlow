# 💸 FinFlow - Microserviço Financeiro com FastAPI, PostgreSQL e Docker

![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-compose-blue)
![PostgreSQL](https://img.shields.io/badge/postgreSQL-15-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

> Um microserviço simples de controle financeiro pessoal, com autenticação, registro de usuários, e cadastro de receitas e despesas. Construído com foco em boas práticas, testes e deploy rápido com Docker Compose.

---

## 🚀 Funcionalidades

- 🔐 Registro de usuários com senha criptografada (bcrypt)
- 🪪 Autenticação via token JWT
- 💰 Cadastro de transações (receitas ou despesas)
- 🧠 Estrutura em microserviço com FastAPI + PostgreSQL
- 🧪 Testes automatizados com Pytest
- 🐳 Docker Compose para infraestrutura local
- 📦 Pronto para escalar com boas práticas de arquitetura

---

## 📁 Estrutura do Projeto

```
finflow/
│
├── app/                  # Lógica da aplicação
│   ├── main.py           # Inicialização da API
│   ├── models.py         # Modelos ORM
│   ├── schemas.py        # Schemas Pydantic
│   ├── database.py       # Conexão com o banco
│   ├── routes.py         # Rotas de API
│   └── auth.py           # Lógica de autenticação
│
├── tests/                # Testes unitários
│   └── test_main.py
│
├── Dockerfile            # Build da imagem Python
├── docker-compose.yml    # Orquestração da app + banco
├── requirements.txt      # Dependências Python
└── README.md             # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.11](https://www.python.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/)**
- **[PostgreSQL 15](https://www.postgresql.org/)**
- **[Docker & Compose](https://docs.docker.com/compose/)**
- **SQLAlchemy + Pydantic**
- **Passlib (bcrypt)** para segurança de senhas
- **python-jose** para JWT

---

## ⚙️ Como rodar localmente

### Pré-requisitos:
- Docker e Docker Compose instalados

### Passos:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/finflow.git
cd finflow

# Suba os containers
docker-compose up --build
```

A API estará disponível em: [http://localhost:8000/docs](http://localhost:8000/docs) 🚀

---

## 🧪 Rodando os testes

```bash
docker exec -it finflow_app pytest
```

---

## 📬 Exemplos de uso

### 🔐 Registro de Usuário

```http
POST /register
{
  "username": "rafael",
  "password": "123456"
}
```

### 💰 Criar Transação

```http
POST /transactions/
{
  "amount": 500.00,
  "type": "income",  // ou "expense"
  "description": "bolsa faculdade"
}
```

---

## ✨ Possíveis melhorias (ideias de extensão)

- [ ] Login com JWT (rota protegida)
- [ ] Vincular transações ao usuário autenticado
- [ ] Listar e filtrar transações por data/tipo
- [ ] Dashboard com gráficos de receitas vs despesas
- [ ] Deploy no Railway / Render

---

## 👤 Autor

Feito com ❤️ por **Rafael Francisco**  
📧 Contato: [seu-email@email.com]

---

## 📄 Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para usar, contribuir e adaptar!