"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd_cycle(n):
    e = 0
    o = 0
    while n / 10 >= 0.1:
        if n % 10 % 2 == 0:
            e = e + 1
        else:
            o = o + 1
        n = n // 10
    return f"even:{e}, odd:{o}"


def even_odd_lst(n):
    if n / 10 <= 0.1:
        if n % 2 == 0:
            return "e"
        else:
            return "o"
    else:
        if n%10%2 == 0:
            return "e" + even_odd_lst(n//10)
        else:
            return "o" + even_odd_lst(n//10)


def even_odd_dict(n):
    if n / 10 <= 0.1:
        if n % 2 == 0:
            return {"e": 1, "o": 0}
        else:
            return {"e": 0, "o": 1}
    else:
        if n % 10 % 2 == 0:
            return {"e":(even_odd_dict(n//10))["e"]+1, "o":(even_odd_dict(n//10))["o"]}
        else:
            return {"e":(even_odd_dict(n//10))["e"], "o":(even_odd_dict(n//10))["o"]+1}


print(f"cycle solution. {even_odd_cycle(11234)}")
even_count = 0
odd_count = 0
for i in even_odd_lst(11234):
    if i == "e":
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"first recursion solution. even:{even_count}, odd:{odd_count}")
print(f"second recursion solution. even:{even_odd_dict(11234)['e']}, odd:{even_odd_dict(11234)['o']}")