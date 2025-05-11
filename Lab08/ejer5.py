from collections import deque


class TreeNode:
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
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1


# ✂️ La función que poda:
def prune_tree(root, target):
    if not root:
        return None


    # Primero podar a los hijitos 🌿
    root.left = prune_tree(root.left, target)
    root.right = prune_tree(root.right, target)


    # Si el nodo no es igual al objetivo y no tiene hijos, ¡se va! ❌
    if root.val != target and not root.left and not root.right:
        return None
    return root
def print_tree_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Quitamos los `None` del final que sobran 🎈
    while result and result[-1] is None:
        result.pop()
    return result


def test_prune_tree():
    print("Test Case 1:")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    pruned1 = prune_tree(tree1.root, 1)
    print(print_tree_level_order(pruned1))  # [1]


    print("Test Case 2:")
    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(1)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.right = TreeNode(1)
    pruned2 = prune_tree(tree2.root, 1)
    print(print_tree_level_order(pruned2))  # [1, 2, 3, 1, None, None, 1]


    print("Test Case 3:")
    tree3 = BinaryTree()
    pruned3 = prune_tree(tree3.root, 1)
    print(print_tree_level_order(pruned3))  # []


    print("Test Case 4:")
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    pruned4 = prune_tree(tree4.root, 4)
    print(print_tree_level_order(pruned4))  # []


    print("Test Case 5:")
    tree5 = BinaryTree()
    tree5.root = TreeNode(5)
    tree5.root.left = TreeNode(5)
    tree5.root.right = TreeNode(5)
    pruned5 = prune_tree(tree5.root, 5)
    print(print_tree_level_order(pruned5))  # [5, 5, 5]


# 🌟 ¡Hora de podar! 🧹
test_prune_tree()