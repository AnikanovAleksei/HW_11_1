import csv
from typing import Dict, List


def get_csv_data_dict(file_name: str) -> List[Dict]:
    """Считывает данные о финансовых операциях из CSV файла и преобразует их в список словарей"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Указываем, что разделитель - точка с запятой
            csv_data = csv.DictReader(file, delimiter=";")
            list_new_dict = []
            for row in csv_data:
                row_new_dict = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"],
                        },
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
                list_new_dict.append(row_new_dict)
            return list_new_dict
    except Exception as e:
        print(f"An error occurred: {e}")  # Дополнение вывода ошибки в случае сбоя
        return [{}]


print(get_csv_data_dict("../data/transactions.csv"))
