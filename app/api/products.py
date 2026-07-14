from fastapi import APIRouter, HTTPException

from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products():
    return ProductService.get_all_products()


@router.get("/{product_id}")
def get_product(product_id: str):
    product = ProductService.get_product_by_id(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.post("/")
def create_product(product: ProductCreate):
    return ProductService.create_product(product.model_dump())


@router.put("/{product_id}")
def update_product(product_id: str, product: ProductUpdate):
    return ProductService.update_product(
        product_id,
        product.model_dump(exclude_unset=True)
    )


@router.delete("/{product_id}")
def delete_product(product_id: str):
    return ProductService.delete_product(product_id)
