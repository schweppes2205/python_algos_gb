"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""


import hashlib

user_name_original = input("Please enter your name: ")
user_pass_original = hashlib.sha256(((input("Please enter your pass: ")) + user_name_original).encode())
print(user_pass_original.hexdigest())

user_name_second_attempt = input("Please enter your name: ")
user_pass_second_attempt = hashlib.sha256(((input("Please enter your pass: ")) + user_name_second_attempt).encode())
print(user_pass_second_attempt.hexdigest())

if user_pass_original.hexdigest() == user_pass_second_attempt.hexdigest():
    print("passwords are identical")
else:
    print("there is something wrong with the pass. Please check that username and pass are the same.")




