
class Trainee:
    """Класс для отслеживания прогресса и успеваемости стажеров"""
    def __init__(
        self, name: str, surname: str, passing_grade: int = 10, score: int = 0
    ) -> None:
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        self.__score = 0
        self.score = score

    @property
    def score(self) -> int:
        """Возвращает значение __score"""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Изменяет значение score после предварительной проверки значения value"""
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        elif value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        else:
            self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        """Проверяет, набрал ли стажер проходной балл."""
        return self.score >= self.passing_grade

# --- Тестирование работы класса ---
if __name__ == "__main__":
    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

    # 1. Создание стажера с начальным баллом 9 и проходным баллом 10
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    # 2. Выполнение домашнего задания и проверка статуса
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 3. Пропуск лекции и проверка статуса
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 4. Проверка валидации (попытка задать отрицательное значение)
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")
