from fastapi import FastAPI

from app.routes.webhook import router as webhook_router
from app.routes.responses import router as responses_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Simulated WhatsApp Webhook",
        description="FastAPI app simulating WhatsApp webhook with idempotency and background processing",
        version="1.0.0",
    )
    app.include_router(webhook_router)
    app.include_router(responses_router)

    return app

app = create_app()
