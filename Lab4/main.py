from typing import Any

num_line = 0
variables = dict()
output = open("out_states.txt", "w", encoding="utf-8")


def print_state(state):
    print(f"S{state}{'' if state == 0 else ' -> '}", file=output, end='')


def isdigit(num: str) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        return False


def replace_variable_to_value(string) -> str:
    new_string = []
    for i in range(len(string)):
        if string[i] in variables:
            new_string.append(str(variables[string[i]]))

        elif not isdigit(string[i]) and string[i] not in \
                {"-", "+", "*", "/", "(", ")", ".", " ", ">", "<", "==", "<=", ">=", "&", "|", "!"}:
            raise ValueError(f"Variable <{string[i]}> is not defined")
        else:
            new_string.append(string[i])

    return ''.join(new_string)


class Calc:
    __math_expression = ""
    __reverse_polish_notation = []

    def __init__(self, math_expression) -> None:
        self.__math_expression = math_expression
        self.__math_expression = replace_variable_to_value(self.__math_expression)

    def __check_expression(self) -> bool:
        if (not all(char.isdigit() or char in "+-*/" or char.isspace() or char in "()"
                    for char in self.__math_expression)):
            return False

        stack = []
        reverse_polish_notation = []
        prev_char = ""

        for char in self.__math_expression:
            if char == "(":
                if prev_char != " " and prev_char != "":
                    return False

                stack.append(char)

            elif char == ")":
                while stack and stack[-1] != "(":
                    reverse_polish_notation.append(stack.pop())

                if not stack:
                    return False

                stack.pop()

            elif char in "+-*/":
                if prev_char != ' ' and prev_char != "(" and (prev_char != "" and char == "-"):
                    return False

                stack.append(char)

            elif char.isdigit():
                if prev_char.isdigit():
                    reverse_polish_notation[-1] += char
                    prev_char = char
                    continue

                if prev_char == '-':
                    reverse_polish_notation.append(stack.pop() + char)
                    prev_char = char
                    continue

                if prev_char != " " and prev_char != "" and prev_char != "(":
                    return False

                reverse_polish_notation.append(char)

            prev_char = char

        if any(char == "(" for char in stack):
            return False

        while stack:
            reverse_polish_notation.append(stack.pop())

        self.__reverse_polish_notation = reverse_polish_notation
        return True

    def calculate(self) -> int:
        if not self.__check_expression():
            raise ValueError("Invalid expression")

        reverse_polish_notation = self.__reverse_polish_notation
        stack = []

        for item in reverse_polish_notation:
            if isdigit(item):
                stack.append(int(item))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                num2 = stack.pop()
                num1 = stack.pop()

                if num1 > 127 or num1 < -128:
                    raise ValueError("The operand is outside the range: " + str(num1))

                if num2 > 127 or num2 < -128:
                    raise ValueError("The operand is outside the range: " + str(num2))

                if item == "+":
                    if num1 + num2 > 127 or num1 + num2 < -128:
                        raise ValueError(f"Overflow: {num1} + {num2} = {num1 + num2}")

                    stack.append(num1 + num2)

                elif item == "-":
                    if num1 - num2 > 127 or num1 - num2 < -128:
                        raise ValueError(f"Overflow: {num1} - {num2} = {num1 - num2}")

                    stack.append(num1 - num2)

                elif item == "*":
                    if num1 * num2 > 127 or num1 * num2 < -128:
                        raise ValueError(f"Overflow: {num1} * {num2} = {num1 * num2}")

                    stack.append(num1 * num2)

                elif item == "/":
                    if num2 == 0:
                        raise ValueError("Division by zero")

                    stack.append(num1 // num2)

        return stack[-1]


def get_value(line) -> str | int:
    variable_name = get_variable(line)
    if '"' in variable_name:
        return variable_name.replace('"', "")
    if variable_name in variables:
        return variables[get_variable(line)]

    try:
        temp = Calc(variable_name)
        res = temp.calculate()
    except Exception as e:
        raise ValueError(e)

    return res


def print_error(e) -> None:
    print(f"Error in line {num_line}: {e}")
    print_state(0)
    exit(1)


def get_variable(line) -> str:
    return line[line.index("(") + 1:line.rindex(")")]


def calculate_bool_expression(expression) -> str:
    expression = expression.replace("(", " ( ").replace(")", " ) ").split()
    expression = replace_variable_to_value(expression)

    if len({">", "<", "==", ">=", "<=", "!="} & set(expression)) == 0:
        raise ValueError("Invalid boolean expression")

    expression = [str(item) for item in expression]
    expression = eval(" ".join(expression))

    return expression


def main() -> None:
    print_state("0")
    global num_line
    code = open("code.txt", "r")  # y1
    bool_expressions_results = []  # y2

    print_state(1)
    for line in code:  # x1
        num_line += 1  # y3
        line = line.strip().rstrip()  # y4

        print_state(2)
        if line.startswith("if "):  # x2
            try:  # x3
                expression = get_variable(line)  # y5
                result = calculate_bool_expression(expression)  # y6
                bool_expressions_results.append(int(result))  # y7
            except Exception as e:
                print_error(e)  # y8

        elif "} else {" in line:  # x4
            bool_expressions_results.append(1 - bool_expressions_results.pop())  # y9
            continue

        elif "}" in line:  # x5
            bool_expressions_results.pop()  # y10
            continue

        elif len(line) == 0 or len(bool_expressions_results) > 0 and not bool_expressions_results[-1]:  # x6
            continue

        elif " = " in line:  # x7
            splitered_line = line.split(" = ")  # y11

            print_state(3)
            if len(splitered_line) != 2:  # x8
                print_error("Invalid variable definition")  # y12

            if not line[0][0].isalpha() and "getdata" not in splitered_line[1] and '"' not in splitered_line[1]:  # x9
                print_error("Variable name must start with a letter")  # y13

            if "getdata" in splitered_line[1]:  # x10
                variables[splitered_line[0]] = input()  # y14
                continue

            if '"' in splitered_line[1]:  # x11
                variables[splitered_line[0]] = splitered_line[1].replace('"', "")  # y15
                continue

            e = -1  # y16
            print_state(4)
            try:  # x3
                calc = Calc(splitered_line[1])
                result = calc.calculate()  # y17
            except Exception as er:
                e = er  # y18

            print_state(5)
            if e != -1:  # x12
                try:  # x3
                    result = calculate_bool_expression(splitered_line[1])  # y19
                except:
                    print_error(e)  # y8

            print_state(6)
            variables[splitered_line[0]] = result  # y20

        elif line.startswith("outdata"):  # x13
            try:  # x3
                print(get_value(line))  # y21
            except Exception as e:
                print_error(e)  # y8

        else:
            print_error("Invalid command")  # y22

        print_state(1)
    print_state(0)


main()
