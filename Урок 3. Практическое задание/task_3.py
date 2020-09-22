"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
from hashlib import sha256


user_input = input("please enter a string: ")
a = set()
b = set()
for i in range(len(user_input)):
    if user_input[0:i] != "" and user_input[0:i] != user_input:
        a.add(user_input[0:i])
        b.add(sha256(user_input[0:i].encode()).hexdigest())
    if user_input[i:len(user_input)] != ""  and user_input[i:len(user_input)] != user_input:
        a.add(user_input[i:len(user_input)+1])
        b.add(sha256(user_input[i:len(user_input)].encode()).hexdigest())
    for j in range(len(user_input)):
        if user_input[i:j] != "" and user_input[i:j] != user_input:
            a.add(user_input[i:j])
            b.add(sha256(user_input[i:j].encode()).hexdigest())
print(f"Different substrings with set: {a}\nSubstrings count: {len(a)}")
print(f"Different substrings with hash in set: {b}\nSubstrings count: {len(b)}")


