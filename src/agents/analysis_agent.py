from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider
from src.agents.base_agent import BaseAgent, minimax_model
from src.config.settings import settings
from src.models.analysis import AgentAnalysisRequest, AgentAnalysisResult

class AnalysisAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)

        self.model = AnthropicModel(
            "MiniMax-M2.7",
            provider=AnthropicProvider(
                base_url=settings.minimax_base_url,
                api_key=settings.minimax_api_key,
            ),
        )

        self.agent = Agent[None, AgentAnalysisResult](
            model=self.model,
            output_type=AgentAnalysisResult,
            retries=3,
            instructions="""You are a high-performance triage agent. 
            Analyze inputs strictly into the requested format.""",
        )

analysis_agent = AnalysisAgent(name="analysis_agent")