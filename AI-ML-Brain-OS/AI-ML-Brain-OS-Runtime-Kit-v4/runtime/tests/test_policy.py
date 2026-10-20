from brain_os.policy import PolicyEngine
def test_allowlisted_tool():
    assert PolicyEngine({"echo"}).authorize_tool("echo").allowed
def test_unknown_tool_denied():
    assert not PolicyEngine({"echo"}).authorize_tool("delete_database").allowed
def test_consequential_action_needs_approval():
    assert not PolicyEngine().authorize_action("publish").allowed
    assert PolicyEngine().authorize_action("publish", True).allowed
