import pytest
from brain_os.contracts import TaskEnvelope
def test_valid_task():
    TaskEnvelope(objective="Research patterns").validate()
def test_empty_objective_rejected():
    with pytest.raises(ValueError): TaskEnvelope(objective=" ").validate()
def test_invalid_risk_rejected():
    with pytest.raises(ValueError): TaskEnvelope(objective="x", risk_class="extreme").validate()
