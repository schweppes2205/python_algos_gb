"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему

Slice метод (revers_3) показывает наискорейший результат - нет сравнений, вычислений, рекурсивных вызовов. Из этого
и вытекает высокая скорость даннй операции.
Самым долгим оказывется рекурсивный метод - revers. скорее всего из-за большого количества вызовов функций и организации
памяти под стэк вызовов.
Профайлер не показывает никаких метрик исполнения, но можно уже сказать, что на входынх данных примера первые две
реализации разворота исполняют 22 вызова, против четырех в последней функции, что говорит о простоте реализации.
"""
from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print("timeit() calculations section")
print(f"first function 'revers(123456789123456789)'. result: {revers(123456789123456789)}")
print(f"timeit() results: {timeit('revers(123456789123456789)', 'from __main__ import revers', number=1000)}")
print(f"second function 'revers(123456789123456789)'. result: {revers_2(123456789123456789)}")
print(f"timeit() results: {timeit('revers_2(123456789123456789)', 'from __main__ import revers_2', number=1000)}")
print(f"third function 'revers_3(123456789123456789)'. result: {revers_3(123456789123456789)}")
print(f"timeit() results: {timeit('revers_3(123456789123456789)', 'from __main__ import revers_3', number=1000)}")
# print(revers_3(123456789123456789))
print("====================================")
print("cProfile calculations section")
print("revers(123456789123456789) section")
cProfile.run('revers(123456789123456789)')
print("----------------")
print("revers_2(123456789123456789) section")
cProfile.run('revers(123456789123456789)')
print("----------------")
print("revers_3(123456789123456789) section")
cProfile.run('revers_3(123456789123456789)')
