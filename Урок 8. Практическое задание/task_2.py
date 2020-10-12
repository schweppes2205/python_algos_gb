"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
from copy import deepcopy

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def insert_new_node(self, new_node_value):
        # if new value is greater or equal to current root value check right child
        if new_node_value >= self.get_root_val():
            # if it's None - put there
            if self.get_right_child() is None:
                self.__set_right_child(BinaryTree(new_node_value))
            # in the other case call the same function for the right child
            else:
                self.right_child.insert_new_node(new_node_value)
        # the same logic with left half
        else:
            if self.get_left_child() is None:
                self.__set_left_child(BinaryTree(new_node_value))
            else:
                self.left_child.insert_new_node(new_node_value)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод записи правого потомка текущей ноды дерева
    def __set_right_child(self, right_child_value):
        self.right_child = right_child_value

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод записи левого потомка текущей ноды дерева
    def __set_left_child(self, left_child_value):
        self.left_child = left_child_value

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # full copy of https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    # just to check the tree structure.
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_child is None and self.left_child is None:
            line = '%s' % self.root
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = '%s' % self.root
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

r = BinaryTree(73)
r.insert_new_node(64)
r.insert_new_node(76)
r.insert_new_node(75)
r.insert_new_node(80)
r.insert_new_node(79)
r.insert_new_node(63)
r.insert_new_node(78)
r.insert_new_node(79)
r.insert_new_node(64)
r.insert_new_node(80)
r.display()

# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left(4)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(12)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())
