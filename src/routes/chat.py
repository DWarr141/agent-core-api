"""Chat routes for the application."""
from fastapi import APIRouter
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

from src.agents.analysis_agent import AnalysisAgent
from src.config.settings import settings
from src.models.agent_response import AgentRequest, AgentResponse

router = APIRouter(prefix="/chat", tags=["Chat Operations"])

minimax_model = AnthropicModel(
    "MiniMax-M2.7",
    provider=AnthropicProvider(
        base_url=settings.minimax_base_url,
        api_key=settings.minimax_api_key,
    ),
)

analysis_agent = AnalysisAgent(name="analysis_agent", model=minimax_model)
@router.post("/", response_model=AgentResponse)
async def analyze_prompt(request: AgentRequest) -> AgentResponse:
    """Analyze a prompt using the analysis agent."""
    result = await analysis_agent.agent.run(request.prompt)
    return result.output