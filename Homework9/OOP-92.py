
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

class HardworkingTrainee(Trainee):
    """Класс трудоголиков"""
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2
 
class AuditTrainee(Trainee):
    """Класс вольнослушателей. Вне зависимости от баллов всегда проходят"""
    def is_passing(self) -> bool:
        return True

class Cohort:
    """Агрегация — Учебная группа"""
    def __init__(self, title: str, trainees: list[Trainee] = None) -> None:
        self.title = title
        self.trainees = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет учащегося в группу."""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Имитирует проведение лекции для всех учащихся группы."""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Возвращает список всех учащихся группы, у которых метод is_passing() возвращает True."""
        return [trainee for trainee in self.trainees if trainee.is_passing()]


# === ТЕСТИРОВАНИЕ ИЗ ТЕКСТА ЗАДАНИЯ ===

# 1. Создаем учащихся разных типов 
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10) 
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10) 
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10) 

# 2. Создаем группу и добавляем студентов 
cohort = Cohort("Python Advanced") 
cohort.add_trainee(std_trainee) 
cohort.add_trainee(hard_trainee) 
cohort.add_trainee(audit_trainee) 

# 3. Проводим лекцию для всей группы (+1 балл всем) 
cohort.conduct_lecture() 

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла) 
hard_trainee.do_homework() 

# 5. Выводим список тех, кто проходит курс 
passing_students = cohort.get_passing_students() 

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===") 
for student in cohort.trainees: 
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}") 

print("\nУспешно зачислены на следующий модуль:") 
for student in passing_students: 
    print(f"- {student.name} {student.surname}")
