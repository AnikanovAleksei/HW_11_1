from typing import Any, Dict, List
from src.csv_data_dict import get_csv_data_dict
from src.processing import filter_by_state, sort_by_date
from src.right_format import get_right_format
from src.utils import get_transactions_dictionary
from src.xlsx_data_dict import get_xlsx_data_dict
from src.find import find_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        "Выберите необходимый пункт меню: \n1. Получить информацию о транзакциях из JSON-файла "
        "\n2. Получить информацию о транзакциях из CSV-файла \n3. Получить информацию о транзакциях из XLSX-файла"
    )

    user_choice = input().strip()

    while user_choice not in ["1", "2", "3"]:
        print(
            "Вы не выбрали файл. Выберите необходимый файл: "
            "\n1. Получить информацию о транзакциях из JSON-файла "
            "\n2. Получить информацию о транзакциях из CSV-файла "
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )
        user_choice = input().strip()

    def get_transactions(choice: str) -> Any:
        """Выбирает нужный путь к файлу в выбранном формате"""
        if choice == "1":
            transactions = get_transactions_dictionary("../data/operations.json")
            return transactions
        elif choice == "2":
            transactions = get_csv_data_dict("../data/transactions.csv")
            return transactions
        elif choice == "3":
            transactions = get_xlsx_data_dict("../data/transactions_excel.xlsx")
            return transactions

    print(
        "Для обработки выбран {}-файл".format(
            "JSON" if user_choice == "1" else "CSV" if user_choice == "2" else "XLSX"
        )
    )
    transactions_step_1 = get_transactions(user_choice)

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    user_status = input().strip().upper()

    while user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {user_status} недоступен")
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_status = input().strip().upper()

    print(f"Операции отфильтрованы по статусу {user_status}")
    transactions_step_2 = filter_by_state(transactions_step_1, user_status)

    print("Отсортировать операции по дате? Да/Нет")
    user_sort_date = input().strip().lower()
    user_sort_order = ""

    if user_sort_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_sort_order = input().strip().lower()

        while user_sort_order not in ["по возрастанию", "по убыванию"]:
            print("Введите: по возрастанию / по убыванию")
            user_sort_order = input().strip().lower()

    def get_transactions_list_by_date(transactions: List[Dict], sort_date: str, sort_order: str) -> Any:
        if sort_date.lower() == "да":
            return sort_by_date(transactions, sort_order == "по возрастанию")
        return transactions

    transactions_step_3 = get_transactions_list_by_date(transactions_step_2, user_sort_date, user_sort_order)

    # Запрашиваем транзакции только в рублях
    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_5 = input().strip().lower()

    def get_transactions_list_rub(transactions: List[Dict], user_input: str) -> Any:
        return (
            [tran for tran in transactions if tran["operationAmount"]["currency"]["code"] == "RUB"]
            if user_input == "да"
            else transactions
        )

    transactions_step_4 = get_transactions_list_rub(transactions_step_3, user_input_5)

    # Запрашиваем фильтрацию по слову в описании
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input_6 = input().strip().lower()
    user_input_7 = ""

    if user_input_6 == "да":
        print("Введите слово:")
        user_input_7 = input().strip().lower()

    def get_transactions_list_by_word(transactions: List[Dict], word: str) -> Any:
        return find_transactions(transactions, word) if word else transactions

    transactions_step_5 = get_transactions_list_by_word(transactions_step_4, user_input_7)

    print("Распечатываю итоговый список транзакций...")
    result = get_right_format(transactions_step_5)
    print(result)


if __name__ == "__main__":
    main()
