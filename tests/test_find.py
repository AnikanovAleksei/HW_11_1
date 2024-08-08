import re

import pytest


def find_transactions(transactions, search_string):
    # Компилируем регулярное выражение для поиска без учета регистра
    search_pattern = re.compile(search_string, re.IGNORECASE)

    # Фильтруем список транзакций
    filtered_transactions = [
        transaction for transaction in transactions if search_pattern.search(transaction["description"])
    ]

    return filtered_transactions


def test_find_transactions_exact_match():
    transactions = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    search_string = "Перевод организации"
    expected_output = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    result = find_transactions(transactions, search_string)
    assert result == expected_output


def test_find_transactions_case_insensitive():
    transactions = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    search_string = "переВод орГанизации"
    expected_output = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    result = find_transactions(transactions, search_string)
    assert result == expected_output


def test_find_transactions_partial_match():
    transactions = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    search_string = "перев"
    expected_output = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    result = find_transactions(transactions, search_string)
    assert result == expected_output


def test_find_transactions_no_match():
    transactions = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {"amount": "18588", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
    ]
    search_string = "закрытие вклада"
    expected_output = []
    result = find_transactions(transactions, search_string)
    assert result == expected_output


if __name__ == "__main__":
    pytest.main()
