from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """Генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for i in transactions:
        yield i["description"]


def card_number_generator(a: int, b: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for x in range(a, b):
        zeros = 16 - len(str(x))
        s = "0" * zeros + str(x)
        yield s[0:4] + " " + s[4:8] + " " + s[8:12] + " " + s[12:16]
