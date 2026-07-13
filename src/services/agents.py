from fastapi import APIRouter, HTTPException
from src.models.agents import AgentCreate, AgentResponse

router = APIRouter(tags=["agents"])
agents: dict[int, AgentResponse] = {}

@router.post("/agents", response_model=AgentResponse)
async def create_agent(agent: AgentCreate) -> AgentResponse:
    """Register a new autonomous execution agent."""
    new_id = len(agents) + 1
    agents[new_id] = AgentResponse(agent_id=new_id, **agent.model_dump())
    return agents[new_id]


@router.get("/agents")
async def get_agents() -> dict[str, list[AgentResponse]]:
    """Retrieve all current registered runtime agents."""
    return {"agents": list(agents.values())}


@router.get("/agents/{agent_id}")
async def get_agent(agent_id: int) -> AgentResponse:
    """Fetch profile records for a single agent via identifier."""
    agent = agents.get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@router.put("/agents/{agent_id}")
async def replace_agent(agent_id: int, agent: AgentCreate) -> AgentResponse:
    """Overwrite an entire target agent resource context."""
    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    agents[agent_id] = AgentResponse(agent_id=agent_id, **agent.model_dump())
    return agents[agent_id]


@router.patch("/agents/{agent_id}/status")
async def update_agent_status(agent_id: int, status: str) -> AgentResponse:
    """Modify the specific tracked status of an existing runtime agent."""
    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    agents[agent_id] = agents[agent_id].model_copy(update={"status": status})
    return agents[agent_id]