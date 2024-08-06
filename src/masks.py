import logging

# Создаем логер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler("masks.log")
file_handler.setLevel(logging.DEBUG)

# Создаем форматер для логирования
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Устанавливаем форматер на обработчик
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(card_number) == 16:
        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.debug(f"Успешно маскирован номер карты: {card_number} -> {masked_card}")
        return masked_card
    elif card_number == "":
        logger.error("Нет номера карты")
        return "Нет номера карты"
    else:
        logger.error(f"Неверный формат номера карты: {card_number}")
        return "Неверный формат номера карты"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая маскирует номер счета"""
    masked_account = "**" + mask_account[-4:]
    logger.debug(f"Успешно маскирован номер счета: {mask_account} -> {masked_account}")
    return masked_account


# Пример использования
if __name__ == "__main__":
    card_number = "1234567812345678"
    masked_card_number = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card_number}")

    account_number = "1234567890123456"
    masked_account_number = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account_number}")

    # Примеры с ошибками
    wrong_card_number = "12345"
    print(get_mask_card_number(wrong_card_number))

    empty_card_number = ""
    print(get_mask_card_number(empty_card_number))


if __name__ == "__main__":
    print(get_mask_card_number("8990922113665226"))
    print(get_mask_card_number(""))
    print(get_mask_account("73654108430135874305"))
