import time
from typing import Any, Callable

# Глобальные константы 
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]" 
TIME_DECIMALS = 8 

# Создаем кастомный декоратор для контроля времени работы функции
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для замера времени выполнения функции. Выводит имя функции и время её работы

    Args:
        func (Callable[..., Any]): Целевая функция, работу которой нужно замерить.

    Returns:
        Callable[..., Any]: Обернутая функция (wrapper), сохраняющая исходный
        результат.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        working_time = round(end_time - start_time, TIME_DECIMALS)
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {working_time} сек.")
        return result

    return wrapper

# Аналитическая функция с декоратором и lambda-сортировкой
@performance_logger
def get_sorted_report(
    report_data: list[dict[str, str | float]]
) -> list[dict[str, str | float]]:
    """
    Принимает список словарей и сортирует отчет по выручке жанров по убыванию

    Args:
        report_data (list[dict[str, str | float]]): 
        Неотсортированный список отчетов

    Returns:
        list[dict[str, str | float]]: 
        Новый список, отсортированный по убыванию выручки.
    """
    # Сортировка по убыванию ключа total_sales с помощью lambda
    return sorted(
        report_data, key=lambda item: float(item["total_sales"]), reverse=True
    )

# Тест программы
if __name__ == "__main__":
    # Вводные данные для тестов
    set_1 = [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55},
    ]   

    set_2 = [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00},
    ]

    set_3 = [{"category": "Drama", "total_sales": 500.00}]

    print("\n=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

     # --- ТЕСТ 1 ---
    print("\n--- ТЕСТ 1 ---")
    report_1 = get_sorted_report(set_1)
    print("Топ категорий по выручке:")
    
    number = 1  # Запускаем ручной счетчик с единицы
    for item in report_1:
        print(f"{number}. {item['category']}: {item['total_sales']}")
        number = number + 1  # Увеличиваем номер для следующей строки

    # --- ТЕСТ 2 ---
    print("\n--- ТЕСТ 2 ---")
    report_2 = get_sorted_report(set_2)
    print("Топ категорий по выручке:")
    
    number = 1  # Счетчик
    for item in report_2:
        print(f"{number}. {item['category']}: {item['total_sales']}")
        number = number + 1

    # --- ТЕСТ 3 ---
    print("\n--- ТЕСТ 3 ---")
    report_3 = get_sorted_report(set_3)
    print("Топ категорий по выручке:")
    
    number = 1  # Счетчик
    for item in report_3:
        print(f"{number}. {item['category']}: {item['total_sales']}")
        number = number + 1
    