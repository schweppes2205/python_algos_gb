"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random


def guess(num, guess_count):
    user_input = int(input("please try to guess a number from 1 to 100: "))
    guess_count -= 1
    if guess_count > 0:
        if user_input == num:
            print("Congrats the guess is correct")
            return
        elif user_input > num:
            print(f"Try another number that is less then previous guess. You have {guess_count} more tries")
            guess(num, guess_count)
        else:
            print(f"Try a number that is more then previous guess. You have {guess_count} more tries")
            guess(num, guess_count)
    else:
        print("You have no more chances")
        return


comp_number = random.randint(1, 100)
guess(comp_number, 10)
