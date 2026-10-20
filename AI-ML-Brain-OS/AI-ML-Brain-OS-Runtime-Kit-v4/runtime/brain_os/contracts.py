from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import uuid

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def new_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:12]}"

@dataclass
class TaskEnvelope:
    objective: str
    actor_id: str = "local_user"
    risk_class: str = "low"
    data_classification: str = "public"
    acceptance_criteria: list[str] = field(default_factory=list)
    max_steps: int = 8
    max_cost_units: int = 100
    run_id: str = field(default_factory=lambda: new_id("run"))
    correlation_id: str = field(default_factory=lambda: new_id("corr"))
    created_at: str = field(default_factory=utc_now)
    schema_version: str = "1.0.0"

    def validate(self):
        if not self.objective.strip():
            raise ValueError("objective must not be empty")
        if self.risk_class not in {"low", "moderate", "high", "critical"}:
            raise ValueError("invalid risk_class")
        if self.data_classification not in {"public", "internal", "confidential", "restricted"}:
            raise ValueError("invalid data_classification")
        if not 1 <= self.max_steps <= 100:
            raise ValueError("max_steps must be between 1 and 100")
        if self.max_cost_units < 1:
            raise ValueError("max_cost_units must be positive")

    def to_dict(self):
        return asdict(self)
