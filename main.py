"""Agent Core API.

This API provides a RESTful interface for managing agents and tasks.
"""


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Agent Core API")


# --- Agent Model Schema ---


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
    # Remvoved duplicate 'status' field since it is inherited from AgentBase


# --- Task Model Schema ---


class TaskBase(BaseModel):
    """Model for the base task."""

    name: str = Field(
        ..., min_length=3, max_length=20, description="The name of the task"
    )
    description: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="The description of the task",
    )
    status: str = Field(..., description="The status of the task")


class TaskCreate(TaskBase):
    """Model for creating a new task."""

    pass


class TaskUpdate(BaseModel):
    """Model for updating an existing task."""

    name: str | None = Field(
        None, min_length=3, max_length=20, description="The name of the task"
    )
    description: str | None = Field(
        None,
        min_length=3,
        max_length=200,
        description="The description of the task",
    )
    status: str | None = Field(None, description="The status of the task")


class TaskResponse(TaskBase):
    """Model for responding with a task."""

    task_id: int = Field(..., description="The id of the task")
    # Removed duplicate 'status' field since it is inherited from TaskBase


# --- In-Memory Storage (Moved below schemas to resolve NameError) ---

agents: dict[int, AgentResponse] = {}
tasks: dict[int, TaskResponse] = {}


# --- Health Check ---


@app.get("/health")
async def health_check():
    """Verify the operational status of the API application layers."""
    return {"status": "ok", "version": "1.0.0"}


# --- Agent CRUD ---


@app.post("/agents", response_model=AgentResponse)
async def create_agent(agent: AgentCreate):
    """Register a new autonomous execution agent."""
    new_id = len(agents) + 1
    agents[new_id] = AgentResponse(agent_id=new_id, **agent.model_dump())
    return agents[new_id]


@app.get("/agents")
async def get_agents():
    """Retrieve all current registered runtime agents."""
    return {"agents": list(agents.values())}


@app.get("/agents/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: int):
    """Fetch profile records for a single agent via identifier."""
    agent = agents.get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@app.put("/agents/{agent_id}", response_model=AgentResponse)
async def replace_agent(agent_id: int, agent: AgentCreate):
    """Overwrite an entire target agent resource context."""
    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    agents[agent_id] = AgentResponse(agent_id=agent_id, **agent.model_dump())
    return agents[agent_id]


@app.patch("/agents/{agent_id}/status", response_model=AgentResponse)
async def update_agent_status(agent_id: int, status: str):
    """Modify the specific tracked status of an existing runtime agent."""
    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    agents[agent_id] = agents[agent_id].model_copy(update={"status": status})
    return agents[agent_id]


# --- Task CRUD ---


@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    """Spawn and catalog a primary entry execution task."""
    new_id = len(tasks) + 1
    tasks[new_id] = TaskResponse(task_id=new_id, **task.model_dump())
    return tasks[new_id]


@app.get("/tasks")
async def get_tasks():
    """Return an un-ordered list of all system task entries."""
    return {"tasks": list(tasks.values())}


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Locate a singular mapped task record schema by standard database index."""
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def replace_task(task_id: int, task: TaskCreate):
    """Execute complete field substitution mapping for a targeted task target."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = TaskResponse(task_id=task_id, **task.model_dump())
    return tasks[task_id]


@app.patch("/tasks/{task_id}/status", response_model=TaskResponse)
async def update_task_status(task_id: int, status: str):
    """Transition the active execution lane pipeline step for a task tracking item."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = tasks[task_id].model_copy(update={"status": status})
    return tasks[task_id]