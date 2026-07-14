from pydantic import BaseModel, Field

class AgentAnalysisRequest(BaseModel):
    prompt: str = Field(description="The prompt to analyze.")

class AgentAnalysisResult(BaseModel):
    summary: str = Field(description="A summary of the analysis.")
    primary_intent: str = Field(description="The primary intent of the analysis.")
    suggested_action: str = Field(
        description="Suggested actions to take based on the analysis."
    )