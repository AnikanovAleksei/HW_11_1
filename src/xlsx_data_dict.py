import pandas as pd
from typing import Dict, List


def get_xlsx_data_dict(file_name: str) -> List[Dict]:
    """Считывает данные о финансовых операциях из Excel файла и преобразует их в список словарей."""
    try:
        df = pd.read_excel(file_name)
        list_new_dict = df.to_dict(orient="records")
        for row in list_new_dict:
            row["operationAmount"] = {
                "amount": row["amount"],
                "currency": {
                    "name": row["currency_name"],
                    "code": row["currency_code"],
                },
            }
            del row["amount"]
            del row["currency_name"]
            del row["currency_code"]
        return list_new_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return [{}]
