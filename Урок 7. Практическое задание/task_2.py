"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import randint


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        middle = len(lst) // 2
        left_part = merge_sort(lst[:middle])
        right_part = merge_sort(lst[middle:])
        res = []
        while len(left_part) >= 1 and len(right_part) >= 1:
            if left_part[0] < right_part[0]:
                res.append(left_part[0])
                left_part.pop(0)
            else:
                res.append(right_part[0])
                right_part.pop(0)
        res += left_part if len(left_part) >= 1 else right_part
    return res


a = [randint(0, 1000000)/100000 for i in range(10)]
print(f"Original list:\t{a}")
print(f"sorted list:\t{merge_sort(a)}")
