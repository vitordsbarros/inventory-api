from fastapi import FastAPI

from app.database import engine, Base
from app.routes.product_route import router as product_router

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Controle de Estoque",
    description="CRUD simples com FastAPI + SQLite",
    version="1.0.0"
)

# Rotas
app.include_router(product_router)


@app.get("/")
def home():
    return {"message": "API de estoque funcionando com sucesso"}