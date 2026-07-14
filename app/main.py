from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.products import router as products_router

app = FastAPI(
    title="FastFood AI",
    version="2.0"
)

app.include_router(health_router)
app.include_router(products_router)


@app.get("/")
async def root():
    return {
        "project": "FastFood AI",
        "status": "running"
    }
