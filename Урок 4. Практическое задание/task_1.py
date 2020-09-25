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
Можно незначительно улучшить результат, вынеся операцию вычисления длинны исходного массива за функцию - func_3
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


test_arr = [i for i in range(10000)]
test_arr_len = len(test_arr)
func_1_timer = timeit.Timer("func_1(test_arr)", "from __main__ import func_1, test_arr")
func_2_timer = timeit.Timer("func_2(test_arr)", "from __main__ import func_2, test_arr")
func_3_timer = timeit.Timer("func_3(test_arr_len)", "from __main__ import func_3,test_arr_len")
print(func_1_timer.timeit(number=100))
print(func_2_timer.timeit(number=100))
print(func_3_timer.timeit(number=100))
test_arr = [i for i in range(10)]
print(func_1(test_arr))
print(func_2(test_arr))
print(func_3(len(test_arr)))
