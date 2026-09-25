import os

class Settings:
    app_name: str = os.getenv("VAHI_NAME", "VAHI")
    ollama_base_url: str = os.getenv(
        "OLLAMA_BASE_URL",
        "http://127.0.0.1:11434"
    )
    model: str = os.getenv("VAHI_MODEL", "")


settings = Settings()