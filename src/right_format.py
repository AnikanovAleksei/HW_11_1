from typing import Dict, List, Any

from src.widget import get_date, mask_account_card

"""transactions_list = [{'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z',
                      'operationAmount': {'amount': 23789.0, 'currency': {'name': 'Peso', 'code': 'UYU'}},
                      'description': 'Открытие вклада', 'from': nan, 'to': 'Счет 23294994494356835683'},
                     {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
                      'operationAmount': {'amount': 30368.0, 'currency': {'name': 'Shilling', 'code': 'TZS'}},
                      'description': 'Перевод с карты на карту', 'from': 'Visa 1959232722494097',
                      'to': 'Visa 6804119550473710'}] """


def get_right_format(transactions: List[Dict]) -> Any:
    """Формирует нужный формат вывода данных по транзакциям"""
    if transactions == []:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        print(f"Всего банковских операций в выборке {len(transactions)}")
        for transaction in transactions:
            date = get_date(transaction["date"])
            description = transaction["description"]
            if description == "Открытие вклада":
                card_account = mask_account_card(transaction["to"])
                print(card_account)
            elif description != "Открытие вклада":
                card_account_1 = mask_account_card(transaction["from"])
                card_account_2 = mask_account_card(transaction["to"])
                card_account = f"{card_account_1} -> {card_account_2}"
            trans_sum = transaction["operationAmount"]["amount"]
            trans_cur = transaction["operationAmount"]["currency"]["name"]
            print(
                f"{date} {description} \n{card_account} \nСумма: {trans_sum} {trans_cur}"
            )
