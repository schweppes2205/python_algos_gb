"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Первый метод - поиск максимума без лишних операций, кроме подсчета встроенной функцией количества вхождений элемента
в массим.
Второй метод незначительно дольше из-за присутствия второго массива, который также нужно обслуживать.
Ускорить можно первый варинат решения путем удаления из массива элементов, которые уже подсчитаны, что бы не проходить
по ним N раз. Результат timeit показывает ускорение решения.
"""
from timeit import timeit
from random import randint

# array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(1, 10) for i in range(randint(100, 100))]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(arr):
    m = 0
    num = 0
    while len(arr) != 0:
        count = arr.count(arr[0])
        if count > m:
            m = count
            num = arr[0]
        arr = list(filter(lambda a: a != arr[0], arr))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(f"timeit for func_1: {timeit('func_1()', 'from __main__ import func_1', number=1000)}")
print(func_2())
print(f"timeit for func_2: {timeit('func_2()', 'from __main__ import func_2', number=1000)}")
print(func_3(array))
print(f"timeit for func_3: {timeit('func_3(array)', 'from __main__ import func_3, array', number=1000)}")