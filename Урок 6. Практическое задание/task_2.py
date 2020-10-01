"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность

Использовать join вместо конкатенации строк, так как каждая операция конкатенации создает новую область памяти,
куда кладется результат сложения двух строк, соответственно рост количества строк для конкатенации растет по арифметической
прогрессии. Пример запуска сложения и join операции на 1000 элементах ниже.
Результаты:
concat: 0.400244184
join: 0.011315450999999976

к моему удивлению проход по листу циклом оказался на несколько порядков быстрее чем конструкция in:
cycle check: 0.0006285220000000202
'in' check: 1.260247968

Нашел для себя модуль ctypes. Как я понял, он позволяет организовать строгую типизацию библиотеками C, что положительно
скажется на производительности python кода. к сожалению с наскока не вышло разобраться с применением этого модуля.
"""
from timeit import Timer



def plus_str(count):
    s = ""
    for i in range(count):
        s += "123"


def join_str(lst):
    s = ""
    s.join(lst)


def check_cycle(lst):
    for i in range(len(lst)):
        if lst[i] == "50000":
            return True
        else:
            return False


def check_in(lst):
    for "50000" in lst:
        return True
    else:
        return False


test01 = Timer("plus_str(1000)", "from __main__ import plus_str")
print(f"concat: {test01.timeit(1000)}")
join_lst = ["123" for i in range(1000)]
test02 = Timer("join_str(join_lst)", "from __main__ import join_str,join_lst")
print(f"join: {test02.timeit(1000)}")
lst = [str(i) for i in range(50010)]
test03 = Timer("check_cycle(lst)", "from __main__ import check_cycle,lst")
print(f"cycle check: {test03.timeit(1000)}")
test04 = Timer("check_in(lst)", "from __main__ import check_in,lst")
print(f"'in' check: {test04.timeit(1000)}")


