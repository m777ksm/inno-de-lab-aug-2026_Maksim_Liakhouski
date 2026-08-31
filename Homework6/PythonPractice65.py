# игра Угадай число
import random

# Генерируем случайное число от 1 до 20
random_number = random.randint(1, 20)

# Вводим счетчик попыток
attempts = 5

print("\n ИГРА - УГАДАЙ ЧИСЛО ")
# Вывод условия игры
print("\n Я загадал число от 1 до 20. У тебя 5 попыток!")

# Запускаем цикл пока не закончатся попытки
while attempts > 0:
    # Просим ввести число
    number = int(input(f"\n Попытка {6 - attempts}. Введите число: "))

    # Проверка числа и вывод результата
    if number == random_number:
        print("\n Ты угадал! Отличная работа. \n")
        break
    elif number > random_number:
        print(f"\n Слишком много! Осталось попыток: {attempts-1}")
    else: 
        print(f"\n Слишком мало! Осталось попыток: {attempts-1}")

    # Смена значений счетчиков цикла
    attempts -=1
    
# При израсходовании попыток Game over с выводом числа
if attempts == 0:
    print(f"\n Игра окончена. Вы не угадали. Загаданное число: {random_number} \n")
