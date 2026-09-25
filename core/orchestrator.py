from models.ollama_client import OllamaClient

class VAHIOrchestrator:
    def __init__(self, model_client: OllamaClient):
        self.model_client = model_client

        self.system_prompt = """
You are VAHI, a local-first personal AI companion.

Your role is to assist the user naturally, clearly, and conversationally.

Principles:
- Be helpful and honest.
- Do not claim to have performed actions that you did not perform.
- Keep answers appropriate to the user's request.
- Remember that you are part of a larger system with memory,
  tools, agents, and other capabilities that will be added later.
"""

    async def process(self, user_message: str) -> str:
        if not user_message.strip():
            raise ValueError("Message cannot be empty.")

        response = await self.model_client.chat(
            message=user_message,
            system_prompt=self.system_prompt,
        )

        return response