import pytest

from src.processing import inform_state


@pytest.fixture
def test_inform_state() -> str:
    return "EXECUTED"


@pytest.fixture
def test_inform_state_1() -> list[dict[str, object]]:
    return inform_state
