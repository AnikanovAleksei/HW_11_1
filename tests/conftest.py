import pytest

from src.processing import info_state


@pytest.fixture
def test_info_state() -> str:
    return "EXECUTED"


@pytest.fixture
def test_info_state_1() -> list[dict[str, object]]:
    return info_state
