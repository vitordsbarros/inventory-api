from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.crud.product_crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    delete_product
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_one(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return product


@router.delete("/{product_id}")
def remove(product_id: int, db: Session = Depends(get_db)):
    product = delete_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return {"message": "Produto removido com sucesso"}