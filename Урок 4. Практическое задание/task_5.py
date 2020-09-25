"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Чем выше порядок искомого числа, тем выгоднее алгоритм решена Эратосфена:
simple method. 10th prime number 29
timeit 0.0030215050000000007
eratosthenes method. 10th prime number 29
timeit 0.023107125
simple method. 100th prime number 541
timeit 0.356344668
eratosthenes method. 100th prime number 541
timeit 0.024708195000000044
simple method. 1000th prime number 7919
timeit 62.076746233
eratosthenes method. 1000th prime number 7919
timeit 0.9701848049999953

Process finished with exit code 0

В силу того, что алгоритм Эратосфена с самого начала уже начинает исключать все НОК текущего числа, он и работает
эффуктивнее. К моему большому сожалению у меня не хватило компонента времени-усидчивости, что бы дописать красиво
использование метода Эратосфена для поиска N числа. Его можно улучшить добавив запоминание массива простых чисел
для перехода на следующий отрезок, а не составление его каждый раз заново, просто увеличивая верхнюю границу решета.
В самом идеальном случае хочется конечно реализовать через рекурсию, но тут недостаточно уже опыта =)) мозг кипит
слишком сильно =))
Как математически оценить сложность в О-нотации я не понимаю.
Мне кажется первый алгоритм - более чем квадратичный, мы каждое число проверяем на простоту и чем дальше, тем больше
необходимо проверять.
Решето Эратосфена = O(N*log(log(N)))
"""
from math import sqrt
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:                                   #O(n)
        t = 1
        is_simple = True
        while t <= n:                                   #O(n)
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosthenes(stop_num):
    arr = [iter for iter in range(stop_num)]
    for j in range(2, int(sqrt(stop_num)), 1):
        if arr[j]:
            for k in range(j ** 2, stop_num, j):
                arr[k] = False
    return arr


def eratosthenes_2(n):
    found = False
    found_num = 0
    # start = 0
    stop = 1000
    while not found:
        arr = [iter for iter in range(stop)]
        for j in range(int(sqrt(stop))):
            if arr[j] and arr[j] != 0 and arr[j] != 1:
                for k in range(j ** 2, stop, j):
                    arr[k] = False
        primes = sorted(set(arr))
        if len(primes) >= n + 1:
            found = True
            found_num = list(primes)[n + 1]
        else:
            # start += 1000
            stop += 1000
    return found_num


# i = int(input('Введите порядковый номер искомого простого числа: '))
print(f"simple method. 10th prime number {simple(10)}")
print(f"timeit {timeit('simple(10)','from __main__ import simple',number=100)}")
print(f"eratosthenes method. 10th prime number {eratosthenes_2(10)}")
print(f"timeit {timeit('eratosthenes_2(10)','from __main__ import eratosthenes_2',number=100)}")
# -----------
print(f"simple method. 100th prime number {simple(100)}")
print(f"timeit {timeit('simple(100)','from __main__ import simple',number=100)}")
print(f"eratosthenes method. 100th prime number {eratosthenes_2(100)}")
print(f"timeit {timeit('eratosthenes_2(100)','from __main__ import eratosthenes_2',number=100)}")
# -----------
print(f"simple method. 1000th prime number {simple(1000)}")
print(f"timeit {timeit('simple(1000)','from __main__ import simple',number=100)}")
print(f"eratosthenes method. 1000th prime number {eratosthenes_2(1000)}")
print(f"timeit {timeit('eratosthenes_2(1000)','from __main__ import eratosthenes_2',number=100)}")