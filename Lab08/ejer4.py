from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    def build_tree_from_list(self, values):
        if not values:
            return
        self.root = Node(values[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(values):
            current = queue.popleft()
            if values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1


def vertical_order_traversal(root):
    if not root:
        return []


    nodes_by_col = defaultdict(list)
    queue = deque([(root, 0)])  # node and its horizontal distance


    while queue:
        node, hd = queue.popleft()
        nodes_by_col[hd].append(node.val)
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))


    # Ordenar las columnitas
    return [nodes_by_col[x] for x in sorted(nodes_by_col)]


# 🧪 Testeamos
def test_vertical_order_traversal():
    print("Test Case 1:")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    print(vertical_order_traversal(tree1.root))  # [[4], [2], [1, 5], [3], [6]]


    print("Test Case 2:")
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    print(vertical_order_traversal(tree2.root))  # [[3], [2], [1]]


    print("Test Case 3:")
    tree3 = BinaryTree()
    print(vertical_order_traversal(tree3.root))  # []


    print("Test Case 4:")
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1])
    print(vertical_order_traversal(tree4.root))  # [[1]]


    print("Test Case 5:")
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print(vertical_order_traversal(tree5.root))  # [[4], [2], [1, 5, 6], [3], [7]]


# Llamamos los tests 🧪✨
test_vertical_order_traversal()
