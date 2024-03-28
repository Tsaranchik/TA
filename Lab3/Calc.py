from typing import Any


# Функция для проверки является ли строка числом
def isdigit(num: str) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        return False


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
        if (not all(char.isdigit() or char in "+-*/" or char.isspace() or char in "({[)}]"
                    for char in self.__math_expression)):
            return False

        # Создаем стек и список для обратной польской записи выражения
        # и строку для хранения предыдущего символа
        stack = []
        reverse_polish_notation = []
        prev_char = ""

        # Удостоверимся, что скобки, операторы и числа расположены правильно
        for char in self.__math_expression:
            # Если символ - скобка, то добавляем ее в стек
            if char in "({[":
                # Если перед скобкой не было пробела, то возвращаем False
                if prev_char != " " and prev_char != "":
                    return False

                stack.append(char)

            # Если символ - закрывающая скобка,
            elif char in ")}]":
                # Переносим все операторы в обратную польскую запись
                # пока не встретим открывающую скобку
                while stack and stack[-1] not in "({[":
                    reverse_polish_notation.append(stack.pop())

                # Вновь проверяем стек на пустоту т.к. в нем могут быть только операторы
                # перед закрывающей скобкой
                if not stack:
                    return False

                # Удаляем из стека открывающую скобку
                stack.pop()

            # Если символ - оператор, то добавляем его в стек
            elif char in "+-*/":
                # Если перед оператором ничего, то возвращаем False
                if prev_char != " " and prev_char not in "({[":
                    return False

                stack.append(char)

            # Если символ - цифра, то добавляем ее в обратную польскую запись
            elif char.isdigit():
                # Если перед цифрой тоже цифра, то добавляем ее к предыдущей цифре
                if prev_char.isdigit():
                    reverse_polish_notation[-1] += char
                    prev_char = char
                    continue

                # Если перед цифрой знак минус, то добавляем его к цифре
                if prev_char == '-':
                    reverse_polish_notation.append(stack.pop() + char)
                    prev_char = char
                    continue

                # Если перед цифрой не было пробела, то возвращаем False
                if prev_char != " " and prev_char != "" and prev_char not in "({[":
                    return False

                reverse_polish_notation.append(char)

            # Обновляем предыдущий символ
            prev_char = char

        # Проверяем остались ли в стеке не закрытые скобки
        # Если остались, то возвращаем False
        if any(char in "({[" for char in stack):
            return False

        # Если в обратной польской записи всего 1 число, то возвращаем False
        if len(reverse_polish_notation) == 1:
            return False

        # Переносим все операторы в обратную польскую запись
        while stack:
            reverse_polish_notation.append(stack.pop())

        self.__reverse_polish_notation = reverse_polish_notation
        return True

    # Публичный метод вычисления результата заданного выражения
    def calculate(self) -> str | int | Any:
        # Если выражение некорректно, то возвращаем "Invalid expression"
        if not self.__check_expression():
            return "Invalid expression"

        reverse_polish_notation = self.__reverse_polish_notation
        stack = []

        # Вычисляем обратную польскую запись
        for item in reverse_polish_notation:
            # Если элемент - число, то добавляем его в стек
            if isdigit(item):
                stack.append(int(item))
            # Если элемент - оператор, то вычисляем результат
            else:
                # Достаем из стека 2 числа
                num2 = stack.pop()
                num1 = stack.pop()

                # Если числа выходят за пределы [-128, 127], то возвращаем "Overflow"
                if num1 > 127 or num1 < -128:
                    return "Overflow: " + str(num1)

                if num2 > 127 or num2 < -128:
                    return "Overflow: " + str(num2)

                # Проводим операцию в зависимости от оператора
                # Если результат выходит за пределы [-128, 127], то возвращаем "Overflow"
                if item == "+":
                    if num1 + num2 > 127 or num1 + num2 < -128:
                        return f"Overflow: {num1} + {num2} = {num1 + num2}"

                    stack.append(num1 + num2)

                elif item == "-":
                    if num1 - num2 > 127 or num1 - num2 < -128:
                        return f"Overflow: {num1} - {num2} = {num1 - num2}"

                    stack.append(num1 - num2)

                elif item == "*":
                    if num1 * num2 > 127 or num1 * num2 < -128:
                        return f"Overflow: {num1} * {num2} = {num1 * num2}"

                    stack.append(num1 * num2)

                elif item == "/":
                    if num2 == 0:
                        return "Division by zero"

                    stack.append(num1 // num2)

        # Результат вычисления хранится в последнем элементе стека - достаем его
        result = stack[-1]

        # И возвращаем его
        return result
