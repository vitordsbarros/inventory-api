# API de Controle de Estoque

Projeto desenvolvido com **Python + FastAPI + SQLite + SQLAlchemy**, com o objetivo de criar uma API simples, organizada e funcional para gerenciamento de produtos em estoque.

Esta API permite realizar operações básicas de CRUD:

* Criar produtos
* Listar produtos
* Buscar produto por ID
* Remover produtos

---

# Tecnologias Utilizadas

* Python 3
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic

---

# Estrutura do Projeto

```text
controle-estoque-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── product_model.py
│   │
│   ├── schemas/
│   │   └── product_schema.py
│   │
│   ├── routes/
│   │   └── product_route.py
│   │
│   └── crud/
│       └── product_crud.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd controle-estoque-api
```

---

## 2. Criar o ambiente virtual

### Windows (PowerShell)

```powershell
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate
```

---

## 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

Caso necessário:

```powershell
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## 5. Executar a aplicação

```powershell
uvicorn app.main:app --reload
```

Se tudo estiver correto, você verá:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# Documentação Interativa (Swagger)

Após iniciar o projeto, acesse:

```text
http://127.0.0.1:8000/docs
```

Lá você poderá testar toda a API diretamente pelo navegador.

---

# Endpoints Disponíveis

## Criar Produto

```http
POST /products/
```

### Exemplo de body

```json
{
  "name": "Notebook Lenovo",
  "description": "Notebook i5 12ª geração",
  "quantity": 10,
  "price": 3500.00
}
```

---

## Listar Todos os Produtos

```http
GET /products/
```

---

## Buscar Produto por ID

```http
GET /products/{product_id}
```

---

## Remover Produto

```http
DELETE /products/{product_id}
```

---

# Banco de Dados

O projeto utiliza **SQLite**, gerando automaticamente o arquivo:

```text
estoque.db
```

Isso facilita bastante o desenvolvimento local sem necessidade de instalar PostgreSQL ou MySQL inicialmente.

---

# Melhorias Futuras

Próximas evoluções recomendadas:

* Atualizar produto (PUT / PATCH)
* Controle de entrada e saída de estoque
* Autenticação com JWT
* Cadastro de usuários
* Níveis de permissão
* PostgreSQL
* Docker
* Deploy em produção
* Logs e monitoramento

---

# Objetivo do Projeto

Este projeto foi criado com foco em:

* aprendizado de backend
* organização profissional de APIs
* construção de portfólio
* preparação para projetos reais de mercado

---

# Autor

Desenvolvido por Vitor S. Barros como projeto de estudo e evolução profissional em backend com Python.
