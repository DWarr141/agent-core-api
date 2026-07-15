"""Chat routes for the application."""
from fastapi import APIRouter
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from src.agents.analysis_agent import AnalysisAgent
from src.config.settings import settings
from src.models.agent_response import AgentRequest, AgentResponse
from src.services.weather import get_weather

router = APIRouter(prefix="/chat", tags=["Chat Operations"])


openrouter_model = OpenRouterModel(
    "minimax/minimax-m3",
    provider=OpenRouterProvider(
        api_key=settings.openrouter_api_key,
    ),
)
analysis_agent = AnalysisAgent(name="analysis_agent", model=openrouter_model)
analysis_agent.agent.tool_plain(get_weather)

@router.post("", response_model=AgentResponse)
async def analyze_prompt(request: AgentRequest) -> AgentResponse:
    """Analyze a prompt using the analysis agent."""
    result = await analysis_agent.agent.run(request.prompt)
    return result.output