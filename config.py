from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values

SECRETS_PATH = Path(__file__).resolve().parent / ".secrets"
REQUIRED_KEYS = (
    "DISCORD_BOT_TOKEN",
    "DISCORD_APPLICATION_ID",
    "DISCORD_PUBLIC_KEY",
    "LLM_ENDPOINT",
    "LLM_TOKEN",
)


@dataclass(frozen=True)
class Settings:
    discord_bot_token: str
    discord_application_id: str
    discord_public_key: str
    llm_endpoint: str
    llm_token: str


def load_settings() -> Settings:
    if not SECRETS_PATH.is_file():
        raise FileNotFoundError(
            f"Missing {SECRETS_PATH.name}. Copy secrets_example to .secrets and fill in values."
        )

    raw = dotenv_values(SECRETS_PATH)
    missing = [key for key in REQUIRED_KEYS if key not in raw]
    if missing:
        raise ValueError(f"Missing keys in .secrets: {', '.join(missing)}")

    return Settings(
        discord_bot_token=raw["DISCORD_BOT_TOKEN"] or "",
        discord_application_id=raw["DISCORD_APPLICATION_ID"] or "",
        discord_public_key=raw["DISCORD_PUBLIC_KEY"] or "",
        llm_endpoint=raw["LLM_ENDPOINT"] or "",
        llm_token=raw["LLM_TOKEN"] or "",
    )
