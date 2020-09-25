"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
Честно для меня остается вопросом, по какой причине мемоизация дает такой прирост производительности.
Как я понимаю происходящее.
Вызывается функция декоратор, куда в качестве входного параметра передается объект функции с рекурсией. Затем идет
проверка, есть ли значение, которое передается входным параметром в декорируемую функцию в кэше, если нет, то нам нужно
выполнить декорируемую функцию, что значит, что она в любом случае выполнится полностью со всеми рекурсивными вызовами,
что бы попасть в кэш в функции декораторе. как я понимаю, декоратор отработает всего один раз, положив в кэш результат
работы рекурсивной декорируемой функции. Очевидно это понимание неверно, цифры говорят сами за себя
В качестве ускорения можно использовать разворот строки через slice.
Метод join + reversed оказывается медленнее мемоизированной рекурсии. прсото как альтернатива.
Предположил, что мемоизация рекурсии на палиндроме может ускориться, но ошибся.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


# num_100 = randint(10000, 1000000)
# num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)
num_100 = 1234321
num_1000 = 123454321
num_10000 = 1234567654321

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

num_100_str = str(num_100)
num_1000_str = str(num_1000)
num_10000_str = str(num_10000)
num_100_str_len = len(num_100_str)
num_1000_str_len = len(num_1000_str)
num_10000_str_len = len(num_10000_str)

print("new variants")
print("slice")
print(
    timeit(
        'num_100_str[num_100_str_len::-1]',
        setup='from __main__ import num_100_str,num_100_str_len',
        number=10000
    )
)
print(
    timeit(
        'num_1000_str[num_1000_str_len::-1]',
        setup='from __main__ import num_1000_str,num_1000_str_len',
        number=10000
    )
)
print(
    timeit(
        'num_10000_str[num_10000_str_len::-1]',
        setup='from __main__ import num_10000_str,num_10000_str_len',
        number=10000
    )
)
print("reversed")
print(
    timeit(
        "''.join(reversed(num_100_str))",
        setup='from __main__ import num_100_str',
        number=10000
    )
)
print(
    timeit(
        "''.join(reversed(num_1000_str))",
        setup='from __main__ import num_1000_str',
        number=10000
    )
)
print(
    timeit(
        "''.join(reversed(num_10000_str))",
        setup='from __main__ import num_10000_str',
        number=10000
    )
)

