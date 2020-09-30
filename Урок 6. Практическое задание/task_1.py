"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Наиболее подходящим примером оказался алгоритм Эратосфена, применяемый для достаточно большого конечного числа.
Для того, что бы увидеть хоть какие-то цифры пришлось его негативно модифицировать, добавив заполнение дополнительного
массива с простыми числами =)
Но даже в этом случае, прирост оказался совершенно незначительным, слишком мало чисел в результирующем массиве даже
при поиске до 10000.
полностью синтетические цифры получилось выделить лишь добавлением ненужных операций генераторного выражения для листа
и перевода его в кортеж. Так же получилось выявить операцию освобождения памяти.

Line #    Mem usage    Increment   Line Contents
================================================
    30     15.6 MiB     15.6 MiB   @profile
    31                             def eratosthenes(stop_num):
    32     15.6 MiB      0.0 MiB       final_arr = []
    33     16.0 MiB      0.1 MiB       arr = [iter for iter in range(stop_num)]
    34
    35     16.0 MiB      0.0 MiB       for j in range(2, int(sqrt(stop_num)), 1):
    36     16.0 MiB      0.0 MiB           if arr[j]:
    37     16.0 MiB      0.0 MiB               for k in range(j ** 2, stop_num, j):
    38     16.0 MiB      0.0 MiB                   arr[k] = False
    39     16.0 MiB      0.0 MiB       for i in arr:
    40     16.0 MiB      0.0 MiB           if i:
    41     16.0 MiB      0.0 MiB               final_arr.append(i)
    42     54.3 MiB      0.5 MiB       temp_arr = [i for i in range(1000000)]
    43     62.0 MiB      7.6 MiB       temp_tup = tuple(temp_arr)
    44     54.3 MiB      0.0 MiB       del temp_arr
    45     16.2 MiB      0.0 MiB       del temp_tup
    46     16.2 MiB      0.0 MiB       return final_arr



Process finished with exit code 0

По неизвестной мне причине, которую к сожалению не удалось выявить, поле increment показывает неверные значения.
по полю mem usage видно изменение потребления памяти на различных стадиях работы функции.
"""
from math import sqrt
from memory_profiler import profile


@profile
def eratosthenes(stop_num):
    final_arr = []
    arr = [iter for iter in range(stop_num)]

    for j in range(2, int(sqrt(stop_num)), 1):
        if arr[j]:
            for k in range(j ** 2, stop_num, j):
                arr[k] = False
    for i in arr:
        if i:
            final_arr.append(i)
    temp_arr = [i for i in range(1000000)]
    temp_tup = tuple(temp_arr)
    del temp_arr
    del temp_tup
    return final_arr


eratosthenes(10000)
