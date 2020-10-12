"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import Counter, deque


class Node:
    def __init__(self, char=None, left_child=None, right_child=None):
        self.char = char
        self.left_child = left_child
        self.right_child = right_child


def create_tree(stat_arr):
    while len(stat_arr) >= 2:
        first_item = stat_arr.popleft()
        second_item = stat_arr.popleft()
        new_score = first_item[1] + second_item[1]
        new_item = [
            Node(left_child=first_item[0], right_child=second_item[0]),
            new_score,
        ]
        for i in range(len(stat_arr)):
            if new_score <= stat_arr[i][1]:
                stat_arr.insert(i, new_item)
                break
        else:
            stat_arr.append(new_item)
    return stat_arr[0][0]


def get_code(target, item, path=''):
    if not isinstance(item, Node):
        if item == target:
            return True, path
        return False, ''
    found, item_path = get_code(target, item.left_child, f"{path}0")
    if found:
        return found, item_path
    return get_code(target, item.right_child, f"{path}1")


def encode_str(str_to_encode, secret_dict):
    return ''.join(secret_dict[i] for i in str_to_encode)


test_str = input("Please enter a string: ")
stat = Counter(test_str)
sorted_stat = deque(sorted(stat.items(), key=lambda j: j[1]))
tree = create_tree(sorted_stat)
# print(get_code(target=' ', item=tree))
secret = {a: b for a in stat.keys() for b in get_code(a, tree)}
print(f"stat information: {stat.items()}")
print(f"secret dictionary: {secret}")
print(f"encoded string: {encode_str(test_str, secret)}")
