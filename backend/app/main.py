from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="QuantNexus API",
    version="0.1.0",
    description="AI Powered Trading Intelligence"
)

app.include_router(health.router)


@app.get("/")
def root():
    return {
        "project": "QuantNexus",
        "status": "running"
    }