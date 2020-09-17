"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def task_07(n):
    if n == 1:
        return 1
    else:
        return n + task_07(n-1)

user_input = int(input("Please enter a number: "))
if task_07(user_input) == user_input * (user_input + 1) / 2:
    print("it's true")
else:
    print("it's not true")