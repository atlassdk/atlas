"""AtlasClient — High-level client for the Atlas Protocol."""
from typing import Optional

class AtlasClient:
    SUPPORTED_ECOSYSTEMS = {"robinhood-chain", "evm", "virtuals"}
    def __init__(self, private_key: Optional[str] = None, ecosystem: str = "robinhood-chain", rpc_url: Optional[str] = None):
        if ecosystem not in self.SUPPORTED_ECOSYSTEMS:
            raise ValueError(f"Unsupported ecosystem: {ecosystem}")
        self.ecosystem = ecosystem
        self._private_key = private_key
        self._rpc_url = rpc_url or {"robinhood-chain": "https://rpc.mainnet.chain.robinhood.com", "evm": "https://eth.llamarpc.com", "virtuals": "https://rpc.virtuals.io"}.get(ecosystem)

    def create_task(self, required_capabilities: list[str], budget: float, parameters: dict, deadline: Optional[int] = None):
        from .task import Task, TaskStatus
        task = Task(task_id=f"0x{id(self):x}", required_capabilities=required_capabilities, budget=budget, parameters=parameters, ecosystem=self.ecosystem)
        task.status = TaskStatus.CREATED
        return task

    def get_ecosystem(self) -> str:
        return self.ecosystem
