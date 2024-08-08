from unittest.mock import patch

import pandas as pd

# Обновленная функция для чтения Excel данных
from src.xlsx_data_dict import get_xlsx_data_dict


def test_get_xlsx_data_dict():
    # Создаем DataFrame, который будет использован для тестов
    test_data = {
        "id": [650703, 3598919, 593027],
        "state": ["EXECUTED", "EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
        "amount": [16210, 29740, 30368],
        "currency_name": ["Sol", "Peso", "Shilling"],
        "currency_code": ["PEN", "COP", "TZS"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
        "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
    }

    test_df = pd.DataFrame(test_data)

    expected_result = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": 16210,
                "currency": {
                    "name": "Sol",
                    "code": "PEN",
                },
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": 29740,
                "currency": {
                    "name": "Peso",
                    "code": "COP",
                },
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "operationAmount": {
                "amount": 30368,
                "currency": {
                    "name": "Shilling",
                    "code": "TZS",
                },
            },
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
    ]

    # Подмениваем pandas.read_excel на возврат нашего тестового DataFrame
    with patch("pandas.read_excel", return_value=test_df):
        result = get_xlsx_data_dict("mock_file.xlsx")
        assert result == expected_result


if __name__ == "__main__":
    test_get_xlsx_data_dict()
