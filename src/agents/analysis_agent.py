"""Analysis agent for the application."""
from typing import Any

from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName

from src.agents.base_agent import BaseAgent
from src.models.agent_response import AgentResponse


class AnalysisAgent(BaseAgent):
    """Analysis agent for the application."""
    def __init__(self, name: str, model: KnownModelName | Any):
        """Initialize the analysis agent."""
        super().__init__(name)
        self.model = model

        self.agent = Agent[None, AgentResponse](
            model=self.model,
            output_type=AgentResponse,
            retries=3,
            instructions="""You are a high-performance triage agent. 
            Analyze inputs strictly into the requested format.""",
        )
