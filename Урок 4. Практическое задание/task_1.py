"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
Задача - заполнить массив четными числами, граница которого - конец исходного массива.
Можно воспользоваться генератором списка, указав в качестве итератора range с шагом 2, конец которого равен длинне
входного массива.

По какой-то причине, если в func_2 передавать просто число = размер исходного массива, замер дает худший результат.
По непонятной мне причине вывод операции вычисления длинны масива из функции во вне негативно влияет на
производительность. Пример func_3.
Полагаю, что вычисление длины массива, натравленного на генератор производить вычисление не один раз, а при каждой
итерации генератора, но подтверждения этому у меня нет. Уменьшение времени выполнения можно посмотреть на примере
замера с именем func_3_timer_second_attempt, где операция вычисления длины массива отделена от генератора исходного
массива.
Спасибо за интересную задачу =)
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(0, len(nums), 2)]
    return new_arr


def func_3(arr_len):
    new_arr = [i for i in range(0, arr_len, 2)]
    return new_arr


func_1_timer = timeit.Timer("""
test_arr = [i for i in range(10000)]
func_1(test_arr)""", "from __main__ import func_1")
func_2_timer = timeit.Timer("""
test_arr = [i for i in range(10000)]
func_2(test_arr)""", "from __main__ import func_2")
func_3_timer = timeit.Timer("""
test_arr_len = len([i for i in range(10000)])
func_3(test_arr_len)""", "from __main__ import func_3")
func_3_timer_second_attempt = timeit.Timer("""
test_arr = [i for i in range(10000)]
test_arr_len = len(test_arr)
func_3(test_arr_len)""", "from __main__ import func_3")
print(func_1_timer.timeit(number=100))
print(func_2_timer.timeit(number=100))
print(func_3_timer.timeit(number=100))
print(func_3_timer_second_attempt.timeit(number=100))
test_arr = [i for i in range(10)]
print(func_1(test_arr))
print(func_2(test_arr))
print(func_3(len(test_arr)))
