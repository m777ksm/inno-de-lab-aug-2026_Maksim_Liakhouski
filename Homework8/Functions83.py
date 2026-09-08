from typing import Any

# Глобальная константа на уровне модуля
DEFAULT_RETURN_INDEX_BASE = 10.0

# Определение функции с аннотациями
def calculate_overdue_fine(
    days_overdue: Any, 
    fine_rate: float, 
    film_name: str
) -> tuple[float,float] | None:
    
    """
    Отказоустойчивая функция расчета штрафа и технического индекса оборачиваемости

    Args:
        days_overdue (Any): количество дней просрочки
        fine_rate (float): штраф за 1 день просрочки
        film_name (str): название фильма

    Returns:
        tuple ([float, float] | None): сумма штрафа, технический индекс оборачиваемости или None при ошибке
    """
    try: 

        # Преобразовать days_overdue в float
        numeric_days = float(days_overdue)

        # Рассчет суммы штрафа
        total_fine = numeric_days * fine_rate

        # Рассчет технического индекса оборачиваемости 
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        # Выводим на печать результат
        print("=== ПРОВЕРКА ВОЗВРАТОВ === \n")
        print(f"Фильм: '{film_name}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index} \n")

        return total_fine, return_index

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_name}': '{e}' \n")
        return None

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_name}': '{e}' \n")
        return None

    except ZeroDivisionError as e:
            print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_name}': '{e}' \n")
            return None
        
    finally:
         print(" --- Проверка транзакции возврата завершена --- \n\n")

# Тест программы и данные для теста
if __name__ == "__main__":
    test_data = [
        ("Matrix", 5, 1.5),
        ("Inception", "пять", 2.0),
        ("Avatar", 0, 2.5),
        ("Interstellar", [3,], 3.0),
    ]

for film, days, fine in test_data:
    calculate_overdue_fine(days, fine, film)
