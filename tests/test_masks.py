from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number("899092211366522") == "Неверный формат номера карты"
    assert get_mask_card_number("") == "Нет номера карты"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
