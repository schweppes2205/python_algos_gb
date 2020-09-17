"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def summation(operand_1, operand_2):
    return operand_1 + operand_2


def subtraction(operand_1, operand_2):
    return operand_1 - operand_2


def mul(operand_1, operand_2):
    return operand_1 * operand_2


def division(operand_1, operand_2):
    if operand_2 == 0:
        return "the second operand for division cannot be 0."
    return operand_1 / operand_2


def cli():
    operation = input("Please type desired operation (+,-,*,/) or 0 for exit: ")
    if operation == "0":
        return True
    elif operation not in ["+", "-", "*", "/"]:
        print(
            f"Your input \"{operation}\" is not valid.")
        cli()
    else:
        operand_01 = input("Please enter first operand: ")
        operand_02 = input("Please enter second operand: ")
        try:
            operand_01 = int(operand_01)
            operand_02 = int(operand_02)
        except Exception:
            print("Operands should be integer")
            cli()
        operations_dict = {
            "+": summation(operand_01, operand_02),
            "-": subtraction(operand_01, operand_02),
            "*": mul(operand_01, operand_02),
            "/": division(operand_01, operand_02),
        }
        print(operations_dict[operation])
        cli()


cli()
