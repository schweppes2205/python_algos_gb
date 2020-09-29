"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

list append: 0.167977559
deque append: 0.10715460100000002
list insert left: 12.417588684
deque append left: 0.0025325620000007376
(default launch ofr timeit)
list rand index access: 240.526922381
deque rand index access: 257.276428205

добавление элементов на deque быстрее, особенно в начало массива данных.
Доступ до произвольной ячейки в случае с листом быстрее, чем deq, хотя необходимо сделать поправку на необходимость
генерации произвольного числа перед каждой итерацией доступа.

"""
from collections import deque
from timeit import Timer
from random import randint

list_ex = []
deque_ex = deque
for i in range(1000):
    list_ex.append(randint(1, 1000))
deque_ex = deque(list_ex)


# append
def experiment_1_lst():
    for j in range(1000):
        list_ex.append(j)
    return


# append
def experiment_1_deq():
    for j in range(1000):
        deque_ex.append(j)
    return


# append left (insert at 0 position for list)
def experiment_2_lst():
    for j in range(100):
        list_ex.insert(0, j)
    return


# append left
def experiment_2_deq():
    for j in range(100):
        deque_ex.appendleft(j)
    return


# rand access
def experiment_3_lst():
    for j in range(100):
        k = randint(0, len(list_ex))
        list_ex[i]
    return


# rand access
def experiment_3_deq():
    for j in range(100):
        k = randint(0, len(deque_ex))
        deque_ex[i]
    return


# experiment_1_lst_timer = Timer("experiment_1_lst()", "from __main__ import experiment_1_lst")
# print(f"list append: {experiment_1_lst_timer.timeit(number=1000)}")
# experiment_1_deq_timer = Timer("experiment_1_deq()", "from __main__ import experiment_1_deq")
# print(f"deque append: {experiment_1_deq_timer.timeit(number=1000)}")
# experiment_2_lst_timer = Timer("experiment_2_lst()", "from __main__ import experiment_2_lst")
# print(f"list insert left: {experiment_2_lst_timer.timeit(number=100)}")
# experiment_2_deq_timer = Timer("experiment_2_deq()", "from __main__ import experiment_2_deq")
# print(f"deque append left: {experiment_2_deq_timer.timeit(number=100)}")
# experiment_3_lst_timer = Timer("experiment_3_lst()", "from __main__ import experiment_3_lst")
# print(f"list rand index access: {experiment_3_lst_timer.timeit()}")
# experiment_3_deq_timer = Timer("experiment_3_deq()", "from __main__ import experiment_3_deq")
# print(f"deque rand index access: {experiment_3_deq_timer.timeit()}")
