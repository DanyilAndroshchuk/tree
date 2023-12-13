"""
1. Те саме дерево
Дано корені двох бінарних дерев p і q, напишіть функцію, щоб перевірити, чи вони однакові.

Два бінарних дерева вважаються однаковими, якщо вони структурно ідентичні, а вузли мають однакове значення.

Приклад 1:
Input: p = [1,2,3], q = [1,2,3] Output: true

Приклад 2:
Input: p = [1,2], q = [1,null,2] Output: false

Приклад 3:
Input: p = [1,2,1], q = [1,1,2] Output: false

Обмеження:
Кількість вузлів в обох деревах знаходиться в діапазоні [ 0, 100]
-104 <= Node.val <= 104
"""


class TreeNode1:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # Базовий випадок: обидва піддерева є порожніми
    if not p and not q:
        return True
    # Обидва піддерева не порожні, порівнюємо їхні значення та рекурсивно порівнюємо ліві та праві піддерева
    elif p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    # Якщо хоча б одне піддерево порожнє, то вони не є однаковими
    else:
        return False


def list_to_tree1(lst):
    # Функція для перетворення бінарного дерева в список
    if not (0 <= len(lst) < 100 and all(-104 <= val <= 104 if val is not None else True for val in lst)):
        raise ValueError("Not valid lst or val")

    if not lst:
        return None
    nodes = [TreeNode1(val) if val is not None else None for val in lst]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            if left_child_idx < len(nodes):
                nodes[i].left = nodes[left_child_idx]
            if right_child_idx < len(nodes):
                nodes[i].right = nodes[right_child_idx]
    return nodes[0]


def check_tree(p_list, q_list):
    p_tree = list_to_tree1(p_list)
    q_tree = list_to_tree1(q_list)
    result = is_same_tree(p_tree, q_tree)
    return result


# Тестимо:
# p1 = [1, 2, 3]
# q1 = [1, 2, 3]
# print(check_tree(p1, q1))
#
# p2 = [1, 2]
# q2 = [1, None, 2]
# print(check_tree(p2, q2))
#
# p3 = [1, 2, 1]
# q3 = [1, 2, 2]
# print(check_tree(p3, q3))

# ______________________________________________________________________________________________________________________

"""
2. Симетричне дерево
Дано root бінарного дерева, перевірте, чи є він дзеркалом самого себе (тобто симетричним відносно свого центру).

Приклад 1:
Input: root = [1,2,2,3,4,4,3] Output: true

Приклад 2:
Input: root = [ 1, 2, 2, null, 3, null, 3] Output: false

Приклад 3:
Input: p = [1,2,1], q = [1,1,2] Output: false

Обмеження:
Кількість вузлів в обох деревах знаходиться в діапазоні [ 0, 1000]
-10 000 <= Node.val <= 10 000
"""


class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lst_to_tree2(lst):
    # Функція для перетворення бінарного дерева в список
    # Перевірка на порожній список
    if not lst:
        return None

    if len(lst) > 1000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 1000]")

    for val in lst:
        if val is not None and (val < -10000 or val > 10000):
            raise ValueError("Node values should be in the range [-10000, 10000]")

    nodes = [TreeNode2(val) if val is not None else None for val in lst]
    root = nodes[0]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            if left_child_idx < len(nodes):
                nodes[i].left = nodes[left_child_idx]
            if right_child_idx < len(nodes):
                nodes[i].right = nodes[right_child_idx]

    return root


def is_symmetric(root):
    def is_mirror(left, right):
        # Базовий випадок: обидва піддерева є порожніми
        if not left and not right:
            return True
        # Один із піддерев порожній, а інший ні
        if not left or not right:
            return False
        # Порівнюємо значення поточних вузлів і рекурсивно порівнюємо їхні піддерева
        return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    # Перевіряємо, чи дерево є симетричним відносно свого центру
    return is_mirror(root, root)


def check_mirror(root):
    # Запускаємо алгоритм перевірки
    root = lst_to_tree2(root)
    return is_symmetric(root)


# Тестуємо:
# root1 = [1, 2, 2, 3, 4, 4, 3]
# root2 = [1, 2, 2, None, 3, None, 3]
# root3 = [1, 2, 1, None, 1, None, 1]
# print(check_mirror(root1))
# print(check_mirror(root2))
# print(check_mirror(root3))

# ______________________________________________________________________________________________________________________

"""
3. Інвертувати бінарне дерево
Маючи корінь бінарного дерева, інвертувати дерево та повернути його корінь.

Приклад 1:
Input: root = [4,2,7,1,3,6,9] Output: [4,7,2,9,6,3,1]

Приклад 2:
Input: root = [2,1,3] Output: [2,3,1]

Приклад 3:
Input: root = [] Output: []

Обмеження:
Кількість вузлів в дереві знаходиться в діапазоні [0, 100]
-100 <= Node.val <= 100
"""


class TreeNode3:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    # Базовий випадок: порожнє дерево
    if not root:
        return None

    # Обмін лівим і правим піддеревами рекурсивно
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root


def list_to_tree(lst):
    # Функція для перетворення списку в бінарне дерево
    if not lst:
        return None

    if len(lst) > 100:
        raise ValueError("The number of nodes in both trees should be in the range [0, 100]")

    for val in lst:
        if val is not None and (val < -100 or val > 100):
            raise ValueError("Node values should be in the range [-100, 100]")

    nodes = [TreeNode3(val) if val is not None else None for val in lst]
    root = nodes[0]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            if left_child_idx < len(nodes):
                nodes[i].left = nodes[left_child_idx]
            if right_child_idx < len(nodes):
                nodes[i].right = nodes[right_child_idx]

    return root


def tree_to_list(root):
    # Функція для перетворення бінарного дерева в список
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # Видаляємо зі списку непотрібні None з кінця
    while result and result[-1] is None:
        result.pop()

    return result


def check_invert(root):
    # Запускаємо алгоритм перевірки
    root = list_to_tree(root)
    root = invert_tree(root)
    return tree_to_list(root)


# Тестуємо:
# root1 = [4, 2, 7, 1, 3, 6, 9]
# root2 = [2, 1, 3]
# root3 = []
# print(check_invert(root1))
# print(check_invert(root2))
# print(check_invert(root3))

# ______________________________________________________________________________________________________________________

"""
4. K-й найменший елемент у BST
Враховуючи корінь бінарного дерева пошуку та ціле число k, поверніть k-те найменше значення (з індексом 1) усіх 
значень вузлів у дереві.

Приклад 1:
Input: root = [3,1,4,null,2], k = 1 Output: 1

Приклад 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3 Output: 3

Обмеження:
Кількість вузлів у дереві дорівнює n
1 <= k <= n <= 10 000
0 <= Node.val <= 10 000
"""


class TreeNode4:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_smallest(root, k):
    # Повертає k-те найменше значення усіх вузлів бінарного дерева пошуку.
    if not root or k <= 0:
        raise ValueError("Invalid input. Root should not be None and k should be greater than 0.")

    def inorder_traversal(node):
        # Функція для виконання інфіксного обходу бінарного дерева
        if not node:
            return []

        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    # Перевірка чи k не перевищує кількість вузлів у дереві
    if not (1 <= k <= len(root) <= 10000):
        raise ValueError("Invalid input. k should be 1 <= k <= len(root) <= 10 000")

    def build_tree(nodes):
        # Перетворюємо вхідний список на об'єкт TreeNode
        if not nodes:
            return None

        root = TreeNode4(nodes[0])
        queue = [root]
        i = 1

        while queue and i < len(nodes):
            current = queue.pop(0)
            if current:
                current.left = TreeNode4(nodes[i]) if nodes[i] is not None else None
                i += 1
                queue.append(current.left)
                if i < len(nodes):
                    current.right = TreeNode4(nodes[i]) if nodes[i] is not None else None
                    i += 1
                    queue.append(current.right)

        return root

    root = build_tree(root)
    inorder_result = inorder_traversal(root)

    if k > len(inorder_result):
        raise ValueError("Invalid input. k exceeds the number of nodes in the tree.")

    return inorder_result[k - 1]


# Тестуємо:
# root1 = [3, 1, 4, None, 2]
# k1 = 1
# print(bst_smallest(root1, k1))
#
# root2 = [5, 3, 6, 2, 4, None, None, 1]
# k2 = 3
# print(bst_smallest(root2, k2))

# ______________________________________________________________________________________________________________________

"""
5. Серіалізація та десеріалізація бінарного дерева
Серіалізація — це процес перетворення структури даних або об’єкта в послідовність бітів, щоб їх можна було зберегти у 
файлі чи буфері пам’яті або передати через мережеве з’єднання для подальшої реконструкції в тому самому чи іншому 
комп’ютерному середовищі.

Розробіть алгоритм для серіалізації та десеріалізації бінарного дерева. Немає обмежень щодо роботи вашого алгоритму 
серіалізації/десеріалізації. Вам просто потрібно переконатися, що двійкове дерево може бути серіалізовано в рядок, 
і цей рядок може бути десеріалізовано в оригінальну структуру дерева.

Пояснення: формат введення/виведення такий самий, як LeetCode серіалізує двійкове дерево. Вам не обов’язково слідувати 
цьому формату, тому, будь ласка, будьте креативними та самостійно придумайте різні підходи.
 
по суті потрібно написати дві функції serialize та deserialize

Приклад 1:
Input: root = [1,2,3,null,null,4,5] Output: [1,2,3,null,null,4,5]

Приклад 2:
Input: root = [] Output: []

Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [0, 10 000].
-1000 <= Node.val <= 1000
"""


class TreeNode5:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree2(lst):
    # Функція для перетворення списку в бінарне дерево
    if not lst:
        return None

    if len(lst) > 10000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 100]")

    for val in lst:
        if val is not None and (val < -1000 or val > 1000):
            raise ValueError("Node values should be in the range [-1000, 1000]")

    nodes = [TreeNode5(val) if val is not None else None for val in lst]
    for i in range(len(nodes)):
        if nodes[i]:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < len(nodes):
                nodes[i].left = nodes[left_child]
            if right_child < len(nodes):
                nodes[i].right = nodes[right_child]

    return nodes[0]


def tree_to_list2(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Видаляємо ззаду нулі, щоб отримати коректний вигляд списку
    while result and result[-1] is None:
        result.pop()

    return result


def serialize_and_deserialize(root):
    # Запускаємо алгоритм серіалізації та десеріалізації
    root = list_to_tree2(root)
    serialized_tree = tree_to_list2(root)
    deserialized_tree = list_to_tree2(serialized_tree)
    return tree_to_list2(deserialized_tree)


# Тестуємо:
# root1 = [1, 2, 3, None, None, 4, 5]
# root2 = []
# print(serialize_and_deserialize(root1))
# print(serialize_and_deserialize(root2))

# ______________________________________________________________________________________________________________________

"""
6. Двійкове дерево Максимальна сума шляху
Шлях у двійковому дереві — це послідовність вузлів, де кожна пара суміжних вузлів у послідовності має ребро, що їх 
з’єднує. Вузол може з’являтися в послідовності не більше одного разу. Зауважте, що шлях не обов’язково повинен проходити 
через корінь.

Сума шляхів — це сума значень вузла в шляху.

Враховуючи корінь бінарного дерева, повертає максимальну суму шляху будь-якого непорожнього шляху.

Приклад 1:
Input: root = [1,2,3] 
Output: 6
Пояснення: оптимальний шлях 2 -> 1 -> 3 із сумою шляхів 2 + 1 + 3 = 6.

Приклад 2:
Input: root = [-10,9,20,null,null,15,7] 
Output: 42 
Пояснення: оптимальний шлях 15 -> 20 -> 7  із сумою шляхів 15 + 20 + 7 = 42

Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [1, 3 * 10 000].
-1000 <= Node.val <= 1000
"""


class TreeNode6:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree3(lst):
    # Функція для перетворення списку в бінарне дерево
    if not lst:
        return None

    if len(lst) > 3 * 10000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 100]")

    for val in lst:
        if val is not None and (val < -1000 or val > 1000):
            raise ValueError("Node values should be in the range [-1000, 1000]")

    nodes = [None if val is None else TreeNode6(val) for val in lst]
    n = len(nodes)
    for i in range(n):
        if nodes[i]:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            nodes[i].left = nodes[left_idx] if left_idx < n else None
            nodes[i].right = nodes[right_idx] if right_idx < n else None

    return nodes[0]


def max_path_sum(root):
    # Функція, що обчислює максимальну суму шляху в бінарному дереві.
    def helper(node):
        nonlocal max_sum

        if not node:
            return 0

        # Обчислення суми для лівого та правого піддерева
        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        # Оновлення максимальної суми
        max_sum = max(max_sum, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)

    max_sum = float('-inf')
    helper(root)

    return max_sum


def check_max_path(root):
    # Запускаємо алгоритм перевірки
    root = list_to_tree3(root)
    return max_path_sum(root)


# Тестуємо
# root1 = [1, 2, 3, None, None, 4, 5]
# root2 = [-10, 9, 20, None, None, 15, 7]
# print(check_max_path(root1))
# print(check_max_path(root2))

# ______________________________________________________________________________________________________________________

"""
7. Камери бінарного дерева
Вам надано корінь бінарного дерева. Ми встановлюємо камери на вузлах дерева, де кожна камера на вузлі може стежити за 
своїм батьком, собою та своїми безпосередніми дочірніми елементами.

Повертає мінімальну кількість камер, необхідних для моніторингу всіх вузлів дерева.

Приклад 1:
IInput: root = [0,0,null,0,0]
Output: 1 
Пояснення: однієї камери достатньо для моніторингу всіх вузлів, якщо її розмістити, як показано.

Приклад 2:
IInput: root = [0,0,null,0,null,0,null,null,0]
Output: 2 
Пояснення: для моніторингу всіх вузлів дерева потрібні принаймні дві камери. На зображенні вище показано одну 
з дійсних конфігурацій розміщення камери.

Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [1, 1000].
Node.val == 0
"""


class TreeNode7:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree5(lst):
    # Функція для перетворення списку в бінарне дерево
    if not lst:
        return None

    if len(lst) > 1000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 1000]")

    for val in lst:
        if val is not None and (val != 0):
            raise ValueError("Node values should be in the range [-1000, 1000]")

    nodes = [None if val is None else TreeNode7(val) for val in lst]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < len(nodes):
                nodes[i].left = nodes[left_child]
            if right_child < len(nodes):
                nodes[i].right = nodes[right_child]

    return nodes[0]


def min_camera_cover(root):
    # Функція для розрахунку мінімальної кількості камер
    def dfs(node):
        nonlocal cameras

        if not node:
            return None

        left = dfs(node.left)
        right = dfs(node.right)

        if left is None and right is None:
            return "leaf"

        if left == "leaf" or right == "leaf":
            cameras += 1
            return "camera"

        if left == "camera" or right == "camera":
            return "covered"

        return None

    cameras = 0
    if dfs(root) is None:
        cameras += 1

    return cameras


def check_min_camera(root):
    # Запускаємо алгоритм перевірки
    root = list_to_tree5(root)
    return min_camera_cover(root)


# Тестуємо:
# root1 = [0, 0, None, 0, 0]
# root2 = [0, 0, None, 0, None, 0, None, None, 0]
# print(check_min_camera(root1))
# print(check_min_camera(root2))

# ______________________________________________________________________________________________________________________

"""
8. Вертикальний обхід бінарного дерева
Враховуючи корінь бінарного дерева, обчисліть обхід у вертикальному порядку бінарного дерева.

Для кожного вузла в позиції (рядок, стовпець) його лівий і правий дочірні елементи будуть у позиціях (рядок + 1, 
стовпець - 1) і (рядок + 1, стовпець + 1) відповідно. Корінь дерева знаходиться в (0, 0).

Обхід у вертикальному порядку бінарного дерева — це список упорядкованостей зверху вниз для кожного індексу стовпця, 
починаючи з крайнього лівого стовпця і закінчуючи крайнім правим стовпцем. В одному рядку та стовпці може бути кілька 
вузлів. У такому випадку відсортуйте ці вузли за їхніми значеннями.

Повертає вертикальний обхід бінарного дерева.

Приклад 1:
Input: root = [3,9,20,null,null,15,7] 
Output: [[9],[3,15],[20],[7]]
Пояснення:
Стовпець -1: у цьому стовпці лише вузол 9.
Стовпець 0: вузли 3 і 15 знаходяться в цьому стовпці в такому порядку зверху вниз.
Стовпець 1: у цьому стовпці є лише вузол 20.
Стовпець 2: лише вузол 7 у цьому стовпці.

Приклад 2:
Input: root = [1,2,3,4,5,6,7] 
Output: [[4],[2],[1,5,6],[3],[7]] 
Пояснення:
Стовпець -2: у цьому стовпці лише вузол 4.
Стовпець -1: у цьому стовпці лише вузол 2.
Стовпець 0: у цьому стовпці знаходяться вузли 1, 5 і 6.
           1 знаходиться вгорі, тому він стоїть першим.
           5 і 6 знаходяться в одній позиції (2, 0), тому ми впорядкуємо їх за значенням, 5 перед 6.
Стовпець 1: у цьому стовпці лише вузол 3.
Стовпець 2: лише вузол 7 у цьому стовпці.

Приклад 3:
Input: root = [1,2,3,4,6,5,7] 
Output: [[4],[2],[1,5,6],[3],[7]] 
Пояснення: Цей випадок точно такий же, як у прикладі 2, але вузли 5 і 6 поміняні місцями.
Зауважте, що рішення залишається незмінним, оскільки 5 і 6 знаходяться в тому самому місці, і їх слід упорядкувати 
за значеннями.

Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [1, 1000].
0 <= Node.val <= 1000
"""

from collections import defaultdict, deque


class TreeNode8:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree8(lst):
    if not lst:
        return None

    if len(lst) > 1000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 1000]")

    for val in lst:
        if val is not None and (val < -1000 or val > 1000):
            raise ValueError("Node values should be in the range [-1000, 1000]")

    root = TreeNode8(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()

        if lst[i] is not None:
            current.left = TreeNode8(lst[i])
            queue.append(current.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode8(lst[i])
            queue.append(current.right)

        i += 1

    return root


def vertical_traversal(root):
    # Ініціалізація хеш-таблиці та черги
    column_table = defaultdict(list)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        # Додаємо вузол в поточний стовпець
        column_table[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Сортуємо вузли за їхніми координатами та групуємо їх за стовпцями
    sorted_columns = sorted(column_table.items())
    result = []

    for col, nodes in sorted_columns:
        nodes.sort()
        result.append([val for _, val in nodes])

    return result


def check_vertical_traversal(root):
    # Запускаємо алгоритм перевірки
    root = list_to_tree8(root)
    return vertical_traversal(root)


# Тестуємо:
# v_root1 = [3, 9, 20, None, None, 15, 7]
# v_root2 = [1, 2, 3, 4, 5, 6, 7]
# v_root3 = [1, 2, 3, 4, 6, 5, 7]
# print(check_vertical_traversal(v_root1))
# print(check_vertical_traversal(v_root2))
# print(check_vertical_traversal(v_root3))

# ______________________________________________________________________________________________________________________

"""
9. Відновити дерево після попереднього обходу (Preorder Traversal)
Ми запускаємо попередній пошук у глибину (DFS) у корені бінарного дерева.

У кожному вузлі цього обходу ми виводимо D тире (де D — глибина цього вузла), а потім виводимо значення цього вузла. 
Якщо глибина вузла дорівнює D, глибина його безпосереднього дочірнього елемента дорівнює D + 1. Глибина кореневого вузла 
дорівнює 0.
Якщо вузол має лише одного дочірнього елемента, цей дочірній елемент гарантовано буде лівим дочірнім.
Враховуючи вихідний обхід цього обходу, відновити дерево та повернути його корінь.

Приклад 1:
Input: traversal = "1-2--3--4-5--6--7" 
Output: [1,2,5,3,4,6,7]

Приклад 2:
Input: traversal = "1-2--3---4-5--6---7" 
Output: [1,2,5,3,null,6,null,4,null,7]

Приклад 3:
Input: traversal = "1-401--349---90--88" 
Output: [1,401,null,349,88,90]

Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [1, 1 000].
0 <= Node.val <= 1 000 000 000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        if not (0 <= val <= 1_000_000_000):
            raise ValueError('val must be in range [0, 1 000 000 000]')
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder):
    # Функція для побудови бінарного дерева на основі поданого обходу у глибину.
    if not preorder:
        return None

    if len(preorder) > 1000:
        raise ValueError("The number of nodes in both trees should be in the range [0, 1000]")

    stack = []
    root = None
    index = 0

    while index < len(preorder):
        depth = 0
        while index < len(preorder) and preorder[index] == '-':
            depth += 1
            index += 1

        value = ""
        while index < len(preorder) and preorder[index] != '-':
            value += preorder[index]
            index += 1

        node = TreeNode(int(value))

        if not stack:
            root = node
            stack.append((node, depth))
        else:
            while stack and stack[-1][1] != depth - 1:
                stack.pop()

            if stack and stack[-1][1] == depth - 1:
                parent = stack[-1][0]

                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

                stack.append((node, depth))

    return root


def print_result(root):
    # Функція для виведення результатів обходу у ширину для перевірки дерева.
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        elif any(queue):
            result.append(None)

    return result


def check_vertical_traversal2(root):
    # Запускаємо алгоритм перевірки
    root = build_tree(root)
    return print_result(root)


# Тестуємо:
# traversal1 = "1-2--3--4-5--6--7"
# traversal2 = "1-2--3---4-5--6---7"
# traversal3 = "1-401--349---90--88"
#
# print(check_vertical_traversal2(traversal1))
# print(check_vertical_traversal2(traversal2))
# print(check_vertical_traversal2(traversal3))
