#Программа калькулятор
print("\n Простой калькулятор \n")
while True :
    try:
        #Ввод первого числа
        number1 = float(input(" Введите первое число: "))
    except ValueError:
        print ("Неверный ввод! Введите число.")
        continue
    try: 
        #Ввод второго числа
        number2 = float(input("\n Введите второе число: "))
    except ValueError:
        print ("\n Неверный ввод! Введите число. \n")
        continue

        #Выбор действия
    operator = (input("\n Выберите оператор (+, -, *, /): "))
    #Выполнение рассчета
    if operator == "+":
        result = number1 + number2
    
    elif operator == "-":
        result = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":
        if number2 == 0:
            result = ("На ноль делить нельзя!")
        else:
            result = number1 / number2
    else:
        result = ("Неверно указано действие")

    #Вывод результата
    print(f"\n Результат: {number1} {operator} {number2} = {result}")

    #Перезапуск или выход
    act = input("\n Для продолжения нажмите Y, для выхода введите любой другой символ: ")
    if act == "Y" or act == "y":
        print("\n =-=-=-= Спасибо за доверие, продолжаем =-=-=-= \n")
    else:
        break
    