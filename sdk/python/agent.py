"""Agent model for Atlas Protocol SDK."""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Agent:
    agent_id: str; owner: str; name: str; uri: str
    capabilities: list[str] = field(default_factory=list)
    execution_wallet: Optional[str] = None; min_fee: float = 0.0
    active: bool = True; total_tasks: int = 0; successful_tasks: int = 0
    reputation_score: float = 0.0; ecosystem: str = "robinhood-chain"

    @property
    def success_rate(self) -> float:
        return (self.successful_tasks / self.total_tasks * 100.0) if self.total_tasks > 0 else 0.0

    def can_perform(self, capability: str) -> bool:
        return capability in self.capabilities
