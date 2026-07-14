"""Models for the analysis agent."""
from pydantic import BaseModel, Field


class AgentAnalysisRequest(BaseModel):
    """Request for the analysis agent."""
    prompt: str = Field(description="The prompt to analyze.")

class AgentAnalysisResult(BaseModel):
    """Result for the analysis agent."""
    summary: str = Field(description="A summary of the analysis.")
    primary_intent: str = Field(description="The primary intent of the analysis.")
    suggested_action: str = Field(
        description="Suggested actions to take based on the analysis."
    )