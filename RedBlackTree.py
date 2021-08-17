# 2b) RED-BLACK TREE


import sys


# Создание класса узлов
class Node():
    def __init__(self, item):
        self.item = item  # ключ
        self.parent = None  # родитель( имеют все,кроме корневой вершины)
        self.left = None  # левый потомок
        self.right = None  # правый потомок
        self.color = 1  # цвет


# создание класса красно-черных деревьев
class RedBlackTree():
    # конструктор класса RBT
    def __init__(self):
        self.TNULL = Node(0)  # узел
        self.TNULL.color = 0  # цвет
        self.TNULL.left = None  # левый потомок
        self.TNULL.right = None  # правый потомок
        self.root = self.TNULL  # корень дерева

    # функции для поиска в дереве
    # Preorder ( корень -> потомок левый -> правый)
    def pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder (левое -> корень -> правое )
    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder(левое-> правое-> корень)
    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # построение дерева
    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.item:  # определение корня дерева
            return node

        if key < node.item:  # определение последущих узлов
            # все потомки в левом поддереве имеют меньший ключ,
            # а в правом больший

            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Балансировка дерева после удаления узла
    def delete_fix(self, x):
        while x != self.root and x.color == 0:  # пока x не корень и черного цвета
            if x == x.parent.left:  # если x ребенок своего родителя
                s = x.parent.right  # s брат/сестра x
                if s.color == 1:  # если s красный, то делаем его черным
                    s.color = 0
                    x.parent.color = 1  # родитель x красный
                    self.left_rotate(x.parent)  # делаем поворот вправо
                    s = x.parent.right  # s - родитель правого поддерева x

                if s.left.color == 0 and s.right.color == 0:  # если правый и левый - черные
                    s.color = 1  # родитель - красный
                    x = x.parent  # x - родитель
                else:
                    if s.right.color == 0:  # если правое поддерево черное, то левое-черное, а узел-красный
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)  # делаем поворот
                        s = x.parent.right

                    s.color = x.parent.color  # назначаем цвету s цвет родителя x
                    x.parent.color = 0  # сам родитель-черный
                    s.right.color = 0  # правый ребенок s - тоже черный
                    self.left_rotate(x.parent)  # левый поворот
                    x = self.root  # x становится корнем
            else:
                s = x.parent.left  # s - родитель левого поддерева x
                if s.color == 1:  # s был красный,становится черным,как и родитель x
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:  # если оба узла-черные, то они становятся коасными
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:  # если левое поддерево-черное,то правое должно стать черным , а сам узел -красным
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)  # левый поворот для s
                        s = x.parent.left  # s - родитель  левого поддерева x

                    s.color = x.parent.color  # s преобретает цвет родителя x
                    x.parent.color = 0  # родитель x и левое поддерево s - черное
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root  # x становится корнем
        x.color = 0

    # замена местами узлов
    def __rb_transplant(self, u, v):
        if u.parent == None:  # если родитель элемента u- null
            self.root = v  # то v - корень дерева
        elif u == u.parent.left:  # в ином случае v - родитель левого поддерева u
            u.parent.left = v
        else:  # вдругом случае v - родитель правого поддерева u
            u.parent.right = v
        v.parent = u.parent

    # удаление узла
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z  # сохраняем цвет в оригинальный
        y_original_color = y.color
        if z.left == self.TNULL:  # если левый дочерний элемент null
            x = z.right  # назначаем правый дочерний элемент для x
            self.__rb_transplant(z, z.right)  # трансплантация (замена)
        elif (z.right == self.TNULL):  # если правый null
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)  # назначаем минимум правого поддерева в y
            y_original_color = y.color  # `сохраняем цвет
            x = y.right  # правый ребенок y - x
            if y.parent == z:  # если наш элемент родитель y, то y родитель x
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)  # замена y и правого ребенка y
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)  # замена y и нашего элемента
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:  # если изначальный цвет черный, то вызываем функцию удаления
            self.delete_fix(x)

    #  Балансировка дерева после добавления узла
    def fix_insert(self, k):
        while k.parent.color == 1:  # пока родительский элемент красный,то делаем следущее :
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:  # если цвет правого дочернего элемента красный,то
                    u.color = 0  # изменяем цвет обоих элементов на черный
                    k.parent.color = 0
                    k.parent.parent.color = 1  # сам элемент оставляем красным
                    k = k.parent.parent  # элемент представялем как новый
                else:
                    if k == k.parent.left:  # производим правый поворот
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0  # цвет элемента меняем на черный, а его предшественника на красный
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)  # левый поворот
            else:
                u = k.parent.parent.right

                if u.color == 1:  # если элемент красный
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:  # если элемент черный
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:  # если элемент-корень,то игнорируем его
                break
        self.root.color = 0  # корень должен быть всегда черным

    # Вывод дерева на экран
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # функции для поиска вглубину в дереве(DFS)
    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    # определение узла с мнимальным ключом
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # определение узла с максимальным ключом
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    # функция наследования
    def successor(self, x):
        if x.right != self.TNULL:  # если правое поддерево не пустое
            return self.minimum(x.right)  # возвращаем минимум из правого поддерева

        y = x.parent  # y - родитель x
        while y != self.TNULL and x == y.right:  # если y не null и cуществует правое поддерево = x, то
            x = y
            y = y.parent
        return y

    #  функция предшествования (аналогично с предыдущей)
    def predecessor(self, x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right  # Назначим x родителем по левому поддереву y
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        # Если родительский элемент x равен NULL, сделаем y корнем дерева.
        # В противном случае, если x является левым дочерним элементом p, сделаем y левым дочерним элементом p.
        # В противном случае назначим y правым потомком p.
        # Изменяем родителя x на родителя y
        # Сделаем y родительским элементом x.
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # Если x имеет правое поддерево,
        # назначьте y в качестве родителя правого поддерева x.
        # Если родительский элемент y равен NULL, сделаем  x корнем дерева.
        # В противном случае, если y является правым дочерним элементом своего родителя p,
        # сделаем x правым дочерним элементом p.
        # В противном случае назначим x как левый дочерний элемент p.
        # Сделаем x родителем y.
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # вставка нового узла
    # осуществляется всегда с красного цвета(потом можно перекрасить или перевернуть)
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None  # лист-NIL
        x = self.root  # корень дерева

        # равен ли x NIL
        while x != self.TNULL:
            y = x  # если да, то конем дерева становится x
            if node.item < x.item:  # сравниваем x с узлами дерева,если узел меньше,
                # то левое поддерево,а если больше,то правое
                x = x.left
            else:
                x = x.right

        node.parent = y  # назначаем родителя узла
        # в качестве родителя вставляемого узла

        # если ключ узла меньше вставляемого, то назначаем его левым узлом,
        # а если нет,то правым, в ином случае,он становится корнем
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        # назначаем null для правого и левого наследника и делаем красным вставляемый узел
        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        # Вызываем алгоритм InsertFix, чтобы сохранить свойство
        # красно-черного дерева в случае нарушения.
        self.fix_insert(node)

    # функция для получения корня
    def get_root(self):
        return self.root

    # функция для удаления узла
    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    # функция для вывода дерева на экран
    def print_tree(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()

    # путем вставки формируем дерево
    print("Введите элементы дерева. Элементы вводятся через пробел. Конец ввода - Enter")
    x = input()
    arr = x.split()
    for i in arr:
        bst.insert(int(i))

    # выводим на экран получившееся красно-черное дерево
    print("Начальное дерево: ")
    bst.print_tree()

    # вывод дерева с добавленным элементом
    new = int(input("Введите элемент,который хотите добавить :  "))
    print("Дерево с добавленным элементом = " + str(new))
    bst.insert(new)
    bst.print_tree()
    # после удаления элемента
    deleted = int(input("Введите элемент,который хотите удалить : "))
    print("Дерево с  удаленным элементом = " + str(deleted))
    bst.delete_node(deleted)
    bst.print_tree()
