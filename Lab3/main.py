from Calc import *

#Главная функция
def main():
    print_state("0")
    # Печатаем предупреждение
    print("Note that the calculator performs operations on numbers that are in this range: [-128, 127]!") #y1

    # Вводим выражение
    math_expression = input("Enter a math expression: ")  # y2
    print_state(1)

    # Создаем объект класса Calc
    caculator = Calc(math_expression)  # y3

    # Выводим результат вычисления
    print(caculator.calculate())  # y4
    print_state(0)


#Запускаем главную функцию
main()
