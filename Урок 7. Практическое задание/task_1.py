"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию

Добавленное условие проверки позволяет выиграть время, в случае если исходный массив уже отсортирован:
time for reverse bubble sort of original list: 0.17782372100000002
ime for reverse bubble sort of sorted array: 0.016341985000000003
"""
from random import randint
from timeit import timeit


def bubble_sort(lst):
    i = 0
    lst_sorted = False
    exchanges_count = 0
    while i != len(lst):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
                exchanges_count += 1
        if exchanges_count == 0:
            break
        i += 1
    return lst


my_lst = [randint(-100, 100) for i in range(1000)]
print(f"original list:\n{my_lst}")
print(f"time for reverse bubble sort of original list: "
      f"{timeit('bubble_sort(my_lst)', setup='from __main__ import bubble_sort, my_lst', number=100)}")
my_lst2 = bubble_sort(my_lst)
print(f"sorted array:\n{my_lst2}")
print(f'time for reverse bubble sort of sorted array: '
      f'{timeit("bubble_sort(my_lst2)", setup="from __main__ import bubble_sort, my_lst2", number=100)}')
print(bubble_sort(my_lst2))
