import pytest
from src.utils import get_transactions_dictionary, return_transaction_amount_in_rub

@pytest.fixture
def get_path():
    return "../data/operations.json"

@pytest.fixture
def get_wrong_path():
    return "nothing"

@pytest.fixture
def get_bad_file():
    return "../data/wrong_operations.json"


def test_get_transactions_dictionary_2(get_wrong_path):
    assert get_transactions_dictionary(get_wrong_path) == []


def test_get_transactions_dictionary_3(get_bad_file):
    assert get_transactions_dictionary(get_bad_file) == []


@pytest.fixture
def transactions():
    return get_transactions_dictionary("../data/operations.json")


@pytest.fixture
def rub_transaction_number():
    return 441945886


@pytest.fixture
def wrong_number():
    return 44194588


def test_return_transaction_amount_in_rub_1(transactions, wrong_number):
    assert return_transaction_amount_in_rub(transactions, wrong_number) == "Транзакция не найдена"
