"""Base agents for the application."""

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

from src.config.settings import settings

if settings.minimax_api_key is None:
    raise ValueError("MINIMAX_API_KEY is not set")


class AgentAnalysisResult(BaseModel):
    """Result of the analysis."""
    summary: str = Field(description="A summary of the analysis.")
    primary_intent: str = Field(description="The primary intent of the analysis.")
    suggested_action: str = Field(
        description="Suggested actions to take based on the analysis."
    )


minimax_model = AnthropicModel(
    "MiniMax-M2.7",
    provider=AnthropicProvider(
        base_url=settings.minimax_base_url,
        api_key=settings.minimax_api_key,
    ),
)

analysis_agent = Agent[None, AgentAnalysisResult](
    model=minimax_model,
    output_type=AgentAnalysisResult,
    retries=3,
    instructions="""You are a high-performance triage agent. 
    Analyze inputs strictly into the requested format.""",
)
