"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import math


def task_4(user_input):
    if user_input == 1:
        return {"num": 1, "str": 1}
    else:
        if user_input % 2 != 0:
            return {"num": task_4(user_input - 1)["num"] + 1 / math.pow(2, user_input - 1),
                    "str": f"{task_4(user_input - 1)['str']} + {1 / math.pow(2, user_input - 1)}"}
        else:
            # return task_4(user_input - 1) - 1 / math.pow(2, user_input - 1)
            return {"num": task_4(user_input - 1)["num"] - 1 / math.pow(2, user_input - 1),
                    "str": f"{task_4(user_input - 1)['str']} - {1 / math.pow(2, user_input - 1)}"}


def main():
    user_input = input("Please enter a number or \"quit\" tp complete the task: ")
    if user_input == "quit":
        return
    else:
        try:
            user_input = int(user_input)
        except Exception:
            print("it must me a number")
            main()
    print(f"operation result: {task_4(user_input)['num']}\nCalculation string: {task_4(user_input)['str']}")
    main()

main()

