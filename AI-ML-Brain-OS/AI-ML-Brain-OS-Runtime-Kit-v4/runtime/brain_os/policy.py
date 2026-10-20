from dataclasses import dataclass

@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str

class PolicyEngine:
    """Default-deny tool policy and approval gate for consequential actions."""
    def __init__(self, allowed_tools=None):
        self.allowed_tools = set(allowed_tools or {"echo"})

    def authorize_tool(self, name):
        return PolicyDecision(name in self.allowed_tools,
                              "allowlisted" if name in self.allowed_tools else f"tool_not_allowlisted:{name}")

    def authorize_action(self, action, approved_by_human=False):
        consequential = {"send_email", "publish", "delete", "purchase", "execute_code"}
        if action in consequential and not approved_by_human:
            return PolicyDecision(False, "human_approval_required")
        return PolicyDecision(True, "allowed")
