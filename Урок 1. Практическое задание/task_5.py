"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self):
        self.stack_obj = []
        self.plate_threshold = 10
        self.active_stack_number = 0

    def push_in(self):
        if len(self.stack_obj) == 0:
            self.stack_obj.append(["plate"])
            print("It's a very first plate here")
        elif len(self.stack_obj[self.active_stack_number]) < self.plate_threshold:
            self.stack_obj[self.active_stack_number].append("plate")
            print(f"Adding a new plate. Now you have: Plate stack number: {self.active_stack_number + 1}."
                  f" Plate number in the last stack: {len(self.stack_obj[self.active_stack_number])}")
        else:
            self.active_stack_number += 1
            self.stack_obj.append(["plate"])
            print(f"We started a new plate stack with number {self.active_stack_number + 1} with one plate.")

    def stack_size(self):
        return self.active_stack_number


if __name__ == '__main__':
    my_stack = StackClass()
    for i in range(25):
        my_stack.push_in()
