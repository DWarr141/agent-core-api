"""Base agents for the application."""

import os
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from src.config.settings import settings

if settings.minimax_api_key is None:
    raise ValueError("MINIMAX_API_KEY is not set")

class AgentAnalysisResult(BaseModel):
    summary: str = Field(description="A summary of the analysis.")
    primary_intent: str = Field(description="The primary intent of the analysis.")
    suggested_action: str = Field(description="Suggested actions to take based on the analysis.")

minimax_model = OpenAIChatModel(
    'MiniMax-M2.7',
    provider=OpenAIProvider(
        base_url=settings.minimax_base_url,
        api_key=settings.minimax_api_key,
    )
)

analysis_agent = Agent(
    model=minimax_model,
    output_type=AgentAnalysisResult,
    retries=3,
    instructions="You are a high-performance triage agent. Analyze inputs strictly into the requested format."
)
