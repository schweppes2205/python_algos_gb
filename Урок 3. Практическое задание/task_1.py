"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from random import randint
import time, datetime


def time_deco(func):
    def wrapper(n):
        print(f"Function name: {func.__name__}. Start time: {datetime.datetime.now().time()}.")
        start_time = time.time()
        func(n)
        stop_time = time.time()
        print(f"Start time: {datetime.datetime.now().time()}.")
        print(f"Execution time: {'{:.2f}'.format(stop_time - start_time)} sec.")
    return wrapper


@time_deco
def fill_lst(n):
    new_lst = []
    for i in range(n):
        new_lst.append(randint(1, 10))
    return


@time_deco
def fill_dict(n):
    new_dict = {}
    for i in range(n):
        new_dict[n] = randint(1, 10)
    return


items_count = 1000000
fill_lst(items_count)
fill_dict(items_count)
