"""Task model for Atlas Protocol SDK."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class TaskStatus(Enum):
    PENDING = "pending"; CREATED = "created"; BIDDING = "bidding"
    EXECUTING = "executing"; VERIFYING = "verifying"; COMPLETED = "completed"
    FAILED = "failed"; DISPUTED = "disputed"

@dataclass
class Task:
    task_id: str; required_capabilities: list[str]; budget: float
    parameters: dict; ecosystem: str; status: TaskStatus = TaskStatus.PENDING
    assigned_agent: Optional[str] = None; created_at: Optional[str] = None
    deadline: Optional[int] = None; result: Optional[dict] = None

    def assign(self, agent_id: str) -> None:
        self.assigned_agent = agent_id; self.status = TaskStatus.EXECUTING

    def complete(self, result: dict) -> None:
        self.result = result; self.status = TaskStatus.COMPLETED

    def fail(self, reason: str) -> None:
        self.status = TaskStatus.FAILED; self.result = {"error": reason}

    @property
    def is_completed(self) -> bool: return self.status == TaskStatus.COMPLETED
