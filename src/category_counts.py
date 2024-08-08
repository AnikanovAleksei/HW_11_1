from collections import Counter


def categorize_transactions(transactions, categories):
    # Инициализируем словарь с категориями и значениями по умолчанию (0)
    category_counts = {category: 0 for category in categories}

    # Инициализируем Counter для подсчета категорий
    counter = Counter()

    # Проходим по каждой транзакции в списке
    for transaction in transactions:
        if transaction.get("state") != "EXECUTED":
            continue  # Пропустить транзакции, которые не выполнены

        description = transaction.get("description", "")

        # Проходим по каждой категории и проверяем, содержится ли она в поле 'description'
        for category in categories:
            if category in description:
                counter[category] += 1

    # Обновляем counts в нашем граничном словаре
    category_counts.update(counter)

    return category_counts


# # Пример использования
# transactions = [
#     {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
#      'operationAmount': {'amount': '16210', 'currency': {'name': 'Sol', 'code': 'PEN'}},
#      'description': 'Перевод организации', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397'},
#     {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
#      'operationAmount': {'amount': '29740', 'currency': {'name': 'Peso', 'code': 'COP'}},
#      'description': 'Перевод с карты на карту', 'from': 'Discover 3172601889670065',
#      'to': 'Discover 0720428384694643'},
#     {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
#      'operationAmount': {'amount': '30368', 'currency': {'name': 'Shilling', 'code': 'TZS'}},
#      'description': 'Перевод с карты на карту', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710'},
#     {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z',
#      'operationAmount': {'amount': '29482', 'currency': {'name': 'Rupiah', 'code': 'IDR'}},
#      'description': 'Перевод с карты на карту', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420'},
#     {'id': '5380041', 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z',
#      'operationAmount': {'amount': '23789', 'currency': {'name': 'Peso', 'code': 'UYU'}},
#      'description': 'Открытие вклада', 'from': '', 'to': 'Счет 23294994494356835683'},
#     {'id': '1962667', 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z',
#      'operationAmount': {'amount': '18588', 'currency': {'name': 'Peso', 'code': 'COP'}},
#      'description': 'Перевод организации', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144'},
#     {'id': '5294458', 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z',
#      'operationAmount': {'amount': '16836', 'currency': {'name': 'Yuan Renminbi', 'code': 'CNY'}},
#      'description': 'Перевод с карты на карту', 'from': 'Visa 2759011965877198', 'to': 'Счет 38287443300766991082'},
#     {'id': '5429839', 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z',
#      'operationAmount': {'amount': '25261', 'currency': {'name': 'Hryvnia', 'code': 'UAH'}},
#      'description': 'Открытие вклада', 'from': '', 'to': 'Счет 76768135089446747029'},
#     {'id': '3226899', 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z',
#      'operationAmount': {'amount': '21680', 'currency': {'name': 'Koruna', 'code': 'CZK'}},
#      'description': 'Открытие вклада', 'from': '', 'to': 'Счет 88329674734590848775'},
#     {'id': '3176764', 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z',
#      'operationAmount': {'amount': '16652', 'currency': {'name': 'Euro', 'code': 'EUR'}},
#      'description': 'Перевод с карты на карту', 'from': 'Mastercard 8387037425051294',
#      'to': 'American Express 5556525473658852'},
#     {'id': '4234093', 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z',
#      'operationAmount': {'amount': '23182', 'currency': {'name': 'Ruble', 'code': 'RUB'}},
#      'description': 'Перевод с карты на карту', 'from': 'Visa 0773092093872450', 'to': 'Discover 8602781449570491'},
#     {'id': '3107343', 'state': 'EXECUTED', 'date': '2023-01-25T13:33:00Z',
#      'operationAmount': {'amount': '33639', 'currency': {'name': 'Krona', 'code': 'SEK'}},
#      'description': 'Открытие вклада', 'from': '', 'to': 'Счет 86795456734903584433'}
# ]
#
# categories = ['Перевод организации', 'Перевод с карты на карту', 'Открытие вклада']
#
# result = categorize_transactions(transactions, categories)
# print(result)
