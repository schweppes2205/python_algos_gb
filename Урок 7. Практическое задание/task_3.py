"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

NOTE:
    к сожалению не могу победить случай, когда в списке встречаются повторения данным механизмом. как я понимаю,
    он заточен для абсолютно рандомного списка.
    Использую алгоритм, расписаный тут https://habr.com/en/post/346930/
    Так же при увеличении количесва элементов в списке:
    lst = [randint(0, 1000000) for i in range(12345)]
    моя реализация алгоритма дает ответ, расходящийся с встроенной функцией median()

arr[m]
from statistics import median
"""
from random import choice, randint
from statistics import median


def median_search(internal_lst, median_index):
    if len(internal_lst) == 1:
        return internal_lst[0]
    else:
        pivotal = choice(internal_lst)
        less_than_pivotal = [i for i in internal_lst if i <= pivotal]
        more_than_pivotal = [i for i in internal_lst if i > pivotal]
        # print(f"piv:\t{pivotal}")
        # print(f"list:\t{lst}")
        # print(f"less:\t{less_than_pivotal}")
        # print(f"more:\t{more_than_pivotal}")
        # print(f"median:\t{median_index}")
        if len(less_than_pivotal) >= median_index:
            return median_search(less_than_pivotal, median_index)
        else:
            return median_search(more_than_pivotal, median_index - len(less_than_pivotal))


lst = [randint(0, 1000000) for i in range(123)]
# lst = [100, 94, 38, 81, 23, 65, 73, 19, 73, 79, 9]
print(f"original list:\t\t{lst}")
print(f"sorted list:\t\t{sorted(lst)}")
print(f"task03 median:\t\t{median_search(lst, round(len(lst) / 2))}")

print(f"internal median:\t{median(lst)}")
