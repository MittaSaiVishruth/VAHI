import os
from typing import Optional

import httpx


class OllamaClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.base_url = (
            base_url
            or os.getenv("OLLAMA_BASE_URL")
            or "http://127.0.0.1:11434"
        )

        self.model = model or os.getenv("VAHI_MODEL")

        if not self.model:
            raise ValueError(
                "VAHI_MODEL is not set. "
                "Set it to the exact model name from `ollama list`."
            )

    async def chat(self, message: str, system_prompt: str = "") -> str:
        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt,
            })

        messages.append({
            "role": "user",
            "content": message,
        })

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }

        async with httpx.AsyncClient(timeout=300) as client:
            response = await client.post(
                f"{self.base_url}/api/chat",
                json=payload,
            )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]