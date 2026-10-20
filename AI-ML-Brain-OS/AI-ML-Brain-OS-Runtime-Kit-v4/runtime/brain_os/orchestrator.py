from dataclasses import dataclass
from .contracts import TaskEnvelope, utc_now
from .policy import PolicyEngine
from .audit import emit_event

@dataclass
class RunResult:
    run_id: str
    status: str
    steps: int
    output: dict
    errors: list[str]

class BrainOrchestrator:
    """Bounded deterministic runtime. No autonomous tool selection from untrusted text."""
    def __init__(self, tools, policy):
        self.tools, self.policy = tools, policy
    def run(self, task: TaskEnvelope):
        task.validate()
        emit_event("run_started", run_id=task.run_id, correlation_id=task.correlation_id,
                   actor_id=task.actor_id, risk_class=task.risk_class)
        if task.risk_class in {"high", "critical"}:
            emit_event("human_review_required", run_id=task.run_id)
            return RunResult(task.run_id, "awaiting_approval", 0, {"objective": task.objective}, [])
        decision = self.policy.authorize_tool("echo")
        if not decision.allowed:
            emit_event("run_blocked", run_id=task.run_id, reason=decision.reason)
            return RunResult(task.run_id, "blocked", 0, {}, [decision.reason])
        result = self.tools.get("echo")(text=task.objective)
        status = "completed" if result.ok else "failed"
        emit_event("run_finished", run_id=task.run_id, status=status, steps=1)
        return RunResult(task.run_id, status, 1,
            {"objective": task.objective, "result": result.data, "completed_at": utc_now()},
            [] if result.ok else [result.error or "unknown"])
