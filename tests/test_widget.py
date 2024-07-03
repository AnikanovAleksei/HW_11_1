import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected",
    [("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"), ("Счет 73654108430135874305", "Счет **4305")],
)
def test_mask_account_card(string, expected: str) -> None:
    assert mask_account_card(string) == expected


@pytest.fixture
def date() -> str:
    return "2018-07-11T02:26:18.671407"


def test_get_data(date: str) -> None:
    assert get_date(date) == "11.07.2018"
