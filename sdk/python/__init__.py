"""Atlas Python SDK — Agent Coordination Layer client library."""
__version__ = "0.1.3"
from .client import AtlasClient
from .agent import Agent
from .task import Task, TaskStatus
__all__ = ["AtlasClient", "Agent", "Task", "TaskStatus"]
