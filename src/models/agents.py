from pydantic import BaseModel, Field

class AgentBase(BaseModel):
    """Base model for an agent."""

    name: str = Field(
        ..., min_length=3, max_length=20, description="The name of the agent"
    )
    description: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="The description of the agent",
    )
    model: str = Field(
        ..., min_length=3, max_length=20, description="The model of the agent"
    )
    status: str = Field(..., description="The status of the agent")


class AgentCreate(AgentBase):
    """Model for creating a new agent."""

    pass


class AgentUpdate(BaseModel):
    """Model for updating an existing agent."""

    name: str | None = Field(
        None, min_length=3, max_length=20, description="The name of the agent"
    )
    description: str | None = Field(
        None,
        min_length=3,
        max_length=200,
        description="The description of the agent",
    )
    model: str | None = Field(
        None, min_length=3, max_length=20, description="The model of the agent"
    )
    status: str | None = Field(None, description="The status of the agent")


class AgentResponse(AgentBase):
    """Model for responding with an agent."""

    agent_id: int = Field(..., description="The id of the agent")