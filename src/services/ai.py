"""AI services for the application."""

from fastapi import APIRouter
from src.agents.analysis_agent import analysis_agent
from src.models.analysis import AgentAnalysisRequest, AgentAnalysisResult

router = APIRouter(prefix="/ai", tags=["AI Operations"])


@router.post("/analyze", response_model=AgentAnalysisResult)
async def analyze_prompt(request: AgentAnalysisRequest) -> AgentAnalysisResult:
    """Pass a user prompt to the MiniMax agent enforcing structural restrictions."""
    result = await analysis_agent.agent.run(request.prompt)

    return result.output
