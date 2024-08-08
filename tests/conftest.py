import pytest

from src.main import transactions
from src.processing import info_state


@pytest.fixture
def test_info_state() -> str:
    return "EXECUTED"


@pytest.fixture
def test_info_state_1() -> list[dict[str, object]]:
    return info_state


@pytest.fixture
def test_transactions() -> list[dict]:
    return transactions
