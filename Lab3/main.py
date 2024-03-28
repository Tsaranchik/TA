from Calc import Calc

#Главная функция
def main():
    # Печатаем предупреждение
    print("Note that the calculator performs operations on numbers that are in this range: [-128, 127]!")

    # Вводим выражение
    math_expression = input("Enter a math expression: ")

    # Создаем объект класса Calc
    caculator = Calc(math_expression)

    # Записываем и выводим результат вычисления
    result = caculator.calculate()
    print(result)


#Запускаем главную функцию
main()