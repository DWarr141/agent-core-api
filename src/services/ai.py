"""AI services for the application."""

from fastapi import APIRouter
from src.agents.base_agents import analysis_agent, AgentAnalysisResult

router = APIRouter(prefix="/ai", tags=["AI Operations"])

@router.post("/analyze", response_model=AgentAnalysisResult)
async def analyze_prompt(prompt: str) -> AgentAnalysisResult:
    """Pass a user prompt to the MiniMax agent enforcing structural restrictions."""
    result = await analysis_agent.run(prompt)
    
    return result.output