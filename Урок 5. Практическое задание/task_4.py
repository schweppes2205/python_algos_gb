"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

генерация у обычного словаря проходит быстрее, чем у ordered, либо за счет реализации генератора, либо за счет
особенностей хранения данных в классе OrderedDict
dict gen: 7.710237356
ord_dict gen: 10.268683959

операции последовательного и произвольного доступа не сильно отличаются.
dict ordered access: 7.350068742999998
ord_dict ordered access: 6.745515878999999
dict rand access: 2.8075314270000007
ord_dict rand access: 2.5796004150000016

задач, на которых можно просмотреть их различие к сожалению не придумал.
"""

from timeit import Timer
from random import randint
from collections import OrderedDict

dict_ex = {i: i ** 2 for i in range(100)}
ord_dict_ex = OrderedDict((i, i ** 2) for i in range(100))


def experiment_3_dict():
    dict_ex[randint(0, 99)]


def experiment_3_ord_dict():
    ord_dict_ex[randint(0, 99)]


experiment_1_dict_timer = Timer("dict_ex = {i: i ** 2 for i in range(100)}", "")
print(f"dict gen: {experiment_1_dict_timer.timeit(number=100000)}")
experiment_1_ord_dict_timer = Timer("ord_dict_ex = OrderedDict((i, i**2) for i in range(100))", "from collections import OrderedDict")
print(f"ord_dict gen: {experiment_1_ord_dict_timer.timeit(number=100000)}")
experiment_2_dict_timer = Timer("""for i in range(100):
                                    dict_ex[i]""",
                                "from __main__ import dict_ex")
print(f"dict ordered access: {experiment_2_dict_timer.timeit(number=1000000)}")
experiment_2_ord_dict_timer = Timer("""for i in range(100):
                                        ord_dict_ex[i]""",
                                    "from __main__ import ord_dict_ex")
print(f"ord_dict ordered access: {experiment_2_ord_dict_timer.timeit(number=1000000)}")
experiment_3_dict_timer = Timer("experiment_3_dict()", "from __main__ import experiment_3_dict")
print(f"dict rand access: {experiment_3_dict_timer.timeit(number=1000000)}")
experiment_3_ord_dict_timer = Timer("experiment_3_ord_dict()", "from __main__ import experiment_3_ord_dict")
print(f"ord_dict rand access: {experiment_3_ord_dict_timer.timeit(number=1000000)}")
