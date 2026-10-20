from brain_os.contracts import TaskEnvelope
from brain_os.orchestrator import BrainOrchestrator
from brain_os.policy import PolicyEngine
from brain_os.tools import ToolRegistry, echo_tool
def runtime():
    tools = ToolRegistry(); tools.register("echo", echo_tool)
    return BrainOrchestrator(tools, PolicyEngine({"echo"}))
def test_low_risk_completes():
    assert runtime().run(TaskEnvelope(objective="test")).status == "completed"
def test_high_risk_waits():
    assert runtime().run(TaskEnvelope(objective="test", risk_class="high")).status == "awaiting_approval"
