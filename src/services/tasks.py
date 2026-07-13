"""Services for tasks."""
from fastapi import APIRouter, HTTPException

from src.models.tasks import TaskCreate, TaskResponse

router = APIRouter(tags=["tasks"])
tasks: dict[int, TaskResponse] = {}


@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate) -> TaskResponse:
    """Spawn and catalog a primary entry execution task."""
    new_id = len(tasks) + 1
    tasks[new_id] = TaskResponse(task_id=new_id, **task.model_dump())
    return tasks[new_id]


@router.get("/tasks")
async def get_tasks() -> dict[str, list[TaskResponse]]:
    """Return an un-ordered list of all system task entries."""
    return {"tasks": list(tasks.values())}


@router.get("/tasks/{task_id}")
async def get_task(task_id: int) -> TaskResponse:
    """Locate a singular mapped task record schema by standard database index."""
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}")
async def replace_task(task_id: int, task: TaskCreate) -> TaskResponse:
    """Execute complete field substitution mapping for a targeted task target."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = TaskResponse(task_id=task_id, **task.model_dump())
    return tasks[task_id]


@router.patch("/tasks/{task_id}/status")
async def update_task_status(task_id: int, status: str) -> TaskResponse:
    """Transition the active execution lane pipeline step for a task tracking item."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = tasks[task_id].model_copy(update={"status": status})
    return tasks[task_id]
