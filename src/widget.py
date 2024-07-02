import src.masks


def mask_account_card(account: str) -> str:
    """Функция общей маскировки карты и счета"""
    if "Счет" in account:
        account = f"Счет {src.masks.get_mask_account(account[:])}"
        return account
    else:
        card = src.masks.get_mask_card_number(account[-16:])
        mask = account.replace(account[-16:], card)
        return mask


def get_date(date: str) -> str:
    """Функция преобразования даты"""
    parts = date[:10].split("-")
    return f"{parts[2]}.{parts[1]}.{parts[0]}"
