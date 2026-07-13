"""Models for tasks."""

from pydantic import BaseModel, Field


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
