"""Base agents for the application."""

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

from src.config.settings import settings

if settings.minimax_api_key is None:
    raise ValueError("MINIMAX_API_KEY is not set")

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

minimax_model = AnthropicModel(
    "MiniMax-M2.7",
    provider=AnthropicProvider(
        base_url=settings.minimax_base_url,
        api_key=settings.minimax_api_key,
    ),
)


