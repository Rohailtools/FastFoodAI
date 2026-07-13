from fastapi import FastAPI

app = FastAPI(
    title="FastFood AI v2",
    version="2.0.0",
    description="AI Restaurant Operating System"
)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "FastFood AI v2",
        "version": "2.0.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
