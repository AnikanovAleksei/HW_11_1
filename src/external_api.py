import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты в рубли"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    else:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
            headers={"apikey": api_key},
        )
        data = response.json()
        return float(data["result"])


# Пример использования функции
if __name__ == "__main__":
    transaction_example = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    print(convert_to_rub(transaction_example))
