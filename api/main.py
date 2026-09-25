from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from core.config import settings
from core.orchestrator import VAHIOrchestrator
from models.ollama_client import OllamaClient


app = FastAPI(
    title="VAHI",
    version="0.1.0",
)


model_client = OllamaClient(
    base_url=settings.ollama_base_url,
    model=settings.model,
)

orchestrator = VAHIOrchestrator(model_client)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "VAHI",
        "model": settings.model,
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await orchestrator.process(
            request.message
        )

        return ChatResponse(response=response)

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )