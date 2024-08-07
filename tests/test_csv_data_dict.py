from unittest.mock import patch, mock_open
from src.csv_data_dict import get_csv_data_dict


def test_csv_data_dict():
    mock_csv_data = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;"
        "Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту\n"
        "593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;"
        "Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту\n"
        "366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;"
        "Discover 0325955596714937;Visa 3820488829287420;Перевод с карты на карту\n"
        "5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;"
        ";Счет 23294994494356835683;Открытие вклада\n"
        "1962667;EXECUTED;2023-10-22T09:43:32Z;18588;Peso;COP;"
        "Mastercard 7286844946221431;Счет 76145988629288763144;Перевод организации\n"
        "5294458;EXECUTED;2022-06-20T18:08:20Z;16836;Yuan Renminbi;CNY;"
        "Visa 2759011965877198;Счет 38287443300766991082;Перевод с карты на карту\n"
        "5429839;EXECUTED;2023-06-23T19:46:34Z;25261;Hryvnia;UAH;"
        ";Счет 76768135089446747029;Открытие вклада\n"
        "3226899;EXECUTED;2023-04-17T09:21:15Z;21680;Koruna;CZK;"
        ";Счет 88329674734590848775;Открытие вклада\n"
    )

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_csv_data_dict("/path/to/transactions.csv")
        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {
                    "amount": "16210",
                    "currency": {"name": "Sol", "code": "PEN"},
                },
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "operationAmount": {
                    "amount": "29740",
                    "currency": {"name": "Peso", "code": "COP"},
                },
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
            },
            {
                "id": "593027",
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "operationAmount": {
                    "amount": "30368",
                    "currency": {"name": "Shilling", "code": "TZS"},
                },
                "description": "Перевод с карты на карту",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
            },
            {
                "id": "366176",
                "state": "EXECUTED",
                "date": "2020-08-02T09:35:18Z",
                "operationAmount": {
                    "amount": "29482",
                    "currency": {"name": "Rupiah", "code": "IDR"},
                },
                "description": "Перевод с карты на карту",
                "from": "Discover 0325955596714937",
                "to": "Visa 3820488829287420",
            },
            {
                "id": "5380041",
                "state": "CANCELED",
                "date": "2021-02-01T11:54:58Z",
                "operationAmount": {
                    "amount": "23789",
                    "currency": {"name": "Peso", "code": "UYU"},
                },
                "description": "Открытие вклада",
                "from": "",
                "to": "Счет 23294994494356835683",
            },
            {
                "id": "1962667",
                "state": "EXECUTED",
                "date": "2023-10-22T09:43:32Z",
                "operationAmount": {
                    "amount": "18588",
                    "currency": {"name": "Peso", "code": "COP"},
                },
                "description": "Перевод организации",
                "from": "Mastercard 7286844946221431",
                "to": "Счет 76145988629288763144",
            },
            {
                "id": "5294458",
                "state": "EXECUTED",
                "date": "2022-06-20T18:08:20Z",
                "operationAmount": {
                    "amount": "16836",
                    "currency": {"name": "Yuan Renminbi", "code": "CNY"},
                },
                "description": "Перевод с карты на карту",
                "from": "Visa 2759011965877198",
                "to": "Счет 38287443300766991082",
            },
            {
                "id": "5429839",
                "state": "EXECUTED",
                "date": "2023-06-23T19:46:34Z",
                "operationAmount": {
                    "amount": "25261",
                    "currency": {"name": "Hryvnia", "code": "UAH"},
                },
                "description": "Открытие вклада",
                "from": "",
                "to": "Счет 76768135089446747029",
            },
            {
                "id": "3226899",
                "state": "EXECUTED",
                "date": "2023-04-17T09:21:15Z",
                "operationAmount": {
                    "amount": "21680",
                    "currency": {"name": "Koruna", "code": "CZK"},
                },
                "description": "Открытие вклада",
                "from": "",
                "to": "Счет 88329674734590848775",
            },
        ]
        assert result == expected_result


if __name__ == "__main__":
    test_csv_data_dict()
