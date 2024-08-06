import json
import logging
import os
from typing import Any

from src.external_api import convert_to_rub

# Создаем отдельный объект логгера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создаем каталог для логов, если он не существует
log_dir = "../logs/"
os.makedirs(log_dir, exist_ok=True)

# Настраиваем FileHandler для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"))
file_handler.setLevel(logging.DEBUG)

# Настраиваем FileFormatter для форматирования записей логов
formatter = logging.Formatter("%(asctime)s: %(filename)s: %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

# Добавляем FileHandler к объекту логгера utils
logger.addHandler(file_handler)


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Getting transaction list starts")
        with open(path, "r", encoding="utf-8") as operations:
            transactions_data = json.load(operations)
            logger.info("Transactions list ready")
            return transactions_data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Error: {str(e)}")
        return []


def return_transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли"""
    logger.info("Getting operation amount starts")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = float(transaction["operationAmount"]["amount"])
                logger.info(f"Operation amount in RUB:{rub_amount}")
                return rub_amount
            else:
                not_rub_amount = float(transaction["operationAmount"]["amount"])
                logger.info(f"Operation amount in USD/EUR:{not_rub_amount}")
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(not_rub_amount, currency), 2)
                if rub_amount != 0:
                    logger.info(f"Operation amount in RUB:{rub_amount}")
                    return rub_amount
                else:
                    logger.error("Operation amount can't be converted to RUB")
                    return "Конвертация не может быть выполнена"
    else:
        logger.error("Transaction not found")
        return "Транзакция не найдена"


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount_in_rub(transactions, 441945886))
