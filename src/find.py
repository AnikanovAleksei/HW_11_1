import re


def find_transactions(transactions, search_string):
    # Компилируем регулярное выражение для поиска без учета регистра
    search_pattern = re.compile(search_string, re.IGNORECASE)

    # Фильтруем список транзакций
    filtered_transactions = [
        transaction for transaction in transactions if search_pattern.search(transaction["description"])
    ]

    return filtered_transactions


# Пример использования
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
]

search_string = "Перевод с карты на карту"
result = find_transactions(transactions, search_string)
for transaction in result:
    print(transaction)
