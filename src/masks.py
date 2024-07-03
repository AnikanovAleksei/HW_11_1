def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif card_number == "":
        return "Нет номера карты"
    else:
        return "Неверный формат номера карты"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая маскирует номер счета"""
    return "**" + mask_account[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("8990922113665226"))
    print(get_mask_card_number(""))
    print(get_mask_account("73654108430135874305"))
