from typing import Any


# Функция для проверки является ли строка числом
def isdigit(num: str) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        return False


out_states = open("out_states.txt", "w")


def print_state(state):
    print(f"S{state}{"" if state == 0 else " -> "}", file=out_states, end="")


class Calc:
    # Приватные поля класса
    __math_expression = ""  # Само выражение в виде строки
    __reverse_polish_notation = []  # Обратная польская запись выражения

    # Конструктор класса
    def __init__(self, math_expression):
        self.__math_expression = math_expression

    # Приватный метод для проверки корректности выражения
    def __check_expression(self) -> bool:
        # Удостоверимся, что в выражении нет недопустимых символов
        print_state(2)
        if (not all(char.isdigit() or char in "+-*/" or char.isspace() or char in "()"  # x1
                    for char in self.__math_expression)):
            return False  # y5

        # Создаем стек и список для обратной польской записи выражения
        # и строку для хранения предыдущего символа
        stack = []  # y6
        reverse_polish_notation = []  # y7
        prev_char = ""  # y8

        # Удостоверимся, что скобки, операторы и числа расположены правильно
        for char in self.__math_expression:  # x2
            print_state(3)
            # Если символ - скобка, то добавляем ее в стек
            if char == "(":  # x3
                # Если перед скобкой не было пробела, то возвращаем False
                if prev_char != " " and prev_char != "":  # x4
                    return False  # y5

                stack.append(char)  # y9

            # Если символ - закрывающая скобка,
            elif char == ")":  # x5
                # Переносим все операторы в обратную польскую запись
                # пока не встретим открывающую скобку
                while stack and stack[-1] != "(":  # x6
                    print_state(5)
                    reverse_polish_notation.append(stack.pop())  # y10

                # Вновь проверяем стек на пустоту т.к. в нем могут быть только операторы
                # перед закрывающей скобкой
                if not stack:  # x7
                    return False  # y5

                # Удаляем из стека открывающую скобку
                stack.pop()  # y11

            # Если символ - оператор, то добавляем его в стек
            elif char in "+-*/":  # x8
                # Если перед оператором ничего, то возвращаем False
                if prev_char != " " and prev_char != "(" and (prev_char != "" and char == "-"):  # x9
                    return False  # y5

                stack.append(char)  # y9

            # Если символ - цифра, то добавляем ее в обратную польскую запись
            elif char.isdigit():  # x10
                # Если перед цифрой тоже цифра, то добавляем ее к предыдущей цифре
                if prev_char.isdigit():  # x11
                    reverse_polish_notation[-1] += char  # y12
                    prev_char = char  # y13
                    continue

                # Если перед цифрой знак минус, то добавляем его к цифре
                if prev_char == '-':  # x12
                    reverse_polish_notation.append(stack.pop() + char)  # y14
                    prev_char = char  # y13
                    continue

                # Если перед цифрой не было пробела, то возвращаем False
                if prev_char != " " and prev_char != "" and prev_char != "(":  # x 13
                    return False  # y5

                reverse_polish_notation.append(char)  # y15

            # Обновляем предыдущий символ
            print_state(4)
            prev_char = char  # y13

        # Проверяем остались ли в стеке не закрытые скобки
        # Если остались, то возвращаем False
        if any(char == "(" for char in stack):  # x14
            return False  # y5

        # Если в обратной польской записи всего 1 число, то возвращаем False
        if len(reverse_polish_notation) == 1:  # x15
            return False  # y5

        # Переносим все операторы в обратную польскую запись
        while stack:  # x16
            print_state(6)
            reverse_polish_notation.append(stack.pop())  # y10

        self.__reverse_polish_notation = reverse_polish_notation  # y16
        return True  # y17

    # Публичный метод вычисления результата заданного выражения
    def calculate(self) -> str | int | Any:
        # Если выражение некорректно, то возвращаем "Invalid expression"
        if not self.__check_expression():  # x17
            print_state(7)
            return "Invalid expression"  # y18
        print_state(7)

        # Два вывода одного и того же состояния, сделанные выше, сделаны для того, чтобы в случае попадания
        # в if состояние вывелось, и в случае не попадания в if оно тоже вывелось.
        # Если же поставить вывод состояния перед if, то S7 выведется раньше чем нужно.
        # Грубо говоря, — это костыль

        reverse_polish_notation = self.__reverse_polish_notation  # y19
        stack = []  # y6

        # Вычисляем обратную польскую запись
        for item in reverse_polish_notation:  # x18
            print_state(8)
            # Если элемент - число, то добавляем его в стек
            if isdigit(item):  # x19
                stack.append(int(item))  # y20
            # Если элемент - оператор, то вычисляем результат
            else:
                # Достаем из стека 2 числа
                num2 = stack.pop()  # y21
                num1 = stack.pop()  # y22

                # Если числа выходят за пределы [-128, 127], то возвращаем "Overflow"
                if num1 > 127 or num1 < -128:  # x20
                    return "The operand is outside the range: " + str(num1)  # y23

                if num2 > 127 or num2 < -128:  # x21
                    return "The operand is outside the range: " + str(num2)  # y24

                # Проводим операцию в зависимости от оператора
                # Если результат выходит за пределы [-128, 127], то возвращаем "Overflow"
                if item == "+":  # x22
                    if num1 + num2 > 127 or num1 + num2 < -128:  # x23
                        return f"Overflow: {num1} + {num2} = {num1 + num2}"  # y25

                    stack.append(num1 + num2)  # y26

                elif item == "-":  # x24
                    if num1 - num2 > 127 or num1 - num2 < -128:  # x25
                        return f"Overflow: {num1} - {num2} = {num1 - num2}"  # y27

                    stack.append(num1 - num2)  # y28

                elif item == "*":  # x26
                    if num1 * num2 > 127 or num1 * num2 < -128:  # x 27
                        return f"Overflow: {num1} * {num2} = {num1 * num2}"  # y29

                    stack.append(num1 * num2)  # y30

                elif item == "/":  # x28
                    if num2 == 0:  # x29
                        return "Division by zero"  # y31

                    stack.append(num1 // num2)  # y32

        # Результат лежит в последнем элементе стека - достаём его и возвращаем
        return f"Result: {stack[-1]}"  # y33
