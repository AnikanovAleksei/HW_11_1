def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая маскирует номер счета"""
    return "**" + mask_account[-4:]
