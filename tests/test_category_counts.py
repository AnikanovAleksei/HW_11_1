import pytest

from src.category_counts import categorize_transactions


@pytest.fixture
def sample_data():
    transactions = [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "2",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "3",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
        {
            "id": "4",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
        },
        {
            "id": "5",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 23294994494356835683",
        },
        {
            "id": "6",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
        {
            "id": "7",
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
        },
        {
            "id": "8",
            "state": "EXECUTED",
            "date": "2023-06-23T19:46:34Z",
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 76768135089446747029",
        },
        {
            "id": "9",
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 88329674734590848775",
        },
        {
            "id": "10",
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "description": "Перевод с карты на карту",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
        },
        {
            "id": "11",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
        },
        {
            "id": "12",
            "state": "EXECUTED",
            "date": "2023-01-25T13:33:00Z",
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 86795456734903584433",
        },
    ]
    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
    return transactions, categories


def test_empty_transactions():
    transactions = []
    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]

    expected_output = {"Перевод организации": 0, "Перевод с карты на карту": 0, "Открытие вклада": 0}

    assert categorize_transactions(transactions, categories) == expected_output


def test_empty_categories(sample_data):
    transactions, _ = sample_data
    categories = []

    expected_output = {}

    assert categorize_transactions(transactions, categories) == expected_output


def test_no_matching_categories(sample_data):
    transactions, _ = sample_data
    categories = ["Закрытие вклада", "Пополнение счета"]

    expected_output = {"Закрытие вклада": 0, "Пополнение счета": 0}

    assert categorize_transactions(transactions, categories) == expected_output
