# Создаем глобальную константу
MAX_RENTAL_BATCH_LIMIT = 150.0 

# Создаем функцию и указываем TYPE HINTS
def calculate_rental_batch(
        quantity: int, 
        rental_rate: float, 
        discount: float = 0.0
        ) -> tuple[float, bool]:
    """
    Функция умножает количество дисков на стоимость их аренды и на коэффициент скидки
    и проверяет превышение лимита автоматического одобрения.

    Args:
        quantity (int): количество дисков
        rental_rate (float): стоимость аренды
        discount (float): размер жанровой скидки (в долях от 1). по умолчанию 0.0

    Returns:
        tuple[float, bool]: кортеж с объектами:
            final_sum (float): сумма партии, округленная до 2 знаков.
            is_limit_exceeded (bool): проверка превышает ли сумма лимит.
    """
    # Расчет суммы заказа с округлением до 2 знаков после запятой
    final_sum = round(quantity * rental_rate * (1 - discount), 2) 

    # Проверка превышения лимита суммой заказа
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    # Получение результата работы функции calculate_rental_batch
    return final_sum, is_limit_exceeded

# Тест функции и вывод на печать результатов
print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

# Партия 1 («Academy Dinosaur»): 30 дисков по 2.99 $ (без скидки) Позиционные аргументы
sum1, is_limit_exceeded = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {sum1}$. Превышение лимита: {is_limit_exceeded}")

# Партия 2 («Affair Prejudice»): 40 дисков по 4.99 $ (скидка 10%) Позиционные аргументы
sum1, is_limit_exceeded = calculate_rental_batch(40, 4.99, 0.1)
print(f"Партия 2 («Affair Prejudice»): Сумма {sum1}$. Превышение лимита: {is_limit_exceeded}")

# Партия 3 («Agent Truman»): 10 дисков по 1.99 $ (без скидки) Именованные аргументы
sum1, is_limit_exceeded = calculate_rental_batch(quantity=10, rental_rate=1.99)
print(f"Партия 3 («Agent Truman»): Сумма {sum1}$. Превышение лимита: {is_limit_exceeded}")

# Партия 4 («African Egg»): 50 дисков по 3.50 $ (скидка 20%) Позиционные и именованные агрументы
sum1, is_limit_exceeded = calculate_rental_batch(50, 3.5, discount=0.2)
print(f"Партия 4 («African Egg»): Сумма {sum1}$. Превышение лимита: {is_limit_exceeded}")
