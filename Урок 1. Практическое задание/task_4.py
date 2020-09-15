"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# O(1) all operations are with const
def authentication(user_data_lst, user_pass):
    if user_data_lst[1]["is_active"]:
        if user_data_lst[0]["pass"] == user_pass:
            return "activated"
        else:
            return "wrong pass"
    else:
        if user_data_lst[0]["pass"] == user_pass:
            return "not active"
        else:
            return "wrong pass"

# O(1)
def activation(database, username):
    database[username][1] = {"is_active": True}

#O(N)
def main_logic(database):
    user_name = input("Please enter your name: ")
    if user_name in database.keys():                                            #O(N)
        user_pass = input("please enter your pass: ")
        if authentication(database[user_name], user_pass) == "activated":
            print("Successful authentication.")
        elif authentication(database[user_name], user_pass) == "wrong pass":
            print("Wrong pass")
        elif authentication(database[user_name], user_pass) == "not active":
            user_answer = input("Do you want to activate it? type yes or no: ")
            if user_answer == "yes":
                activation(database, user_name)
                print(f"Now you activated: {database[user_name]}")
            else:
                print("no actions are done")
    else:
        print("no such user")


main_logic(
    {
        "user_1": [{"pass": "pass_1"}, {"is_active": True}],
        "user_2": [{"pass": "pass_2"}, {"is_active": False}],
        "user_3": [{"pass": "pass_3"}, {"is_active": True}],
        "user_4": [{"pass": "pass_4"}, {"is_active": True}],
        "user_5": [{"pass": "pass_5"}, {"is_active": False}],
        "user_6": [{"pass": "pass_6"}, {"is_active": True}],
        "user_7": [{"pass": "pass_0"}, {"is_active": False}],
    }
)
