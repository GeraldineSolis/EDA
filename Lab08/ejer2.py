from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value            # Value of the node
        self.left = None              # Left child
        self.right = None             # Right child

class BinaryTree:
    def __init__(self):
        self.root = None              # Root node of the binary tree

    def build_tree_from_list(self, values):
        if not values:
            return None
        self.root = TreeNode(values[0])    # Initialize root
        queue = deque([self.root])         # Queue for BFS
        index = 1
        while queue and index < len(values):
            node = queue.popleft()
            if values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1

def serialize(root):
    if not root:
        return ""
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.value))  # Store value
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")           # Use "null" for missing nodes
    return ",".join(result)                # Convert list to CSV string

def deserialize(data):
    if not data:
        return None
    values = data.split(",")
    root = TreeNode(int(values[0]))        # Create root
    queue = deque([root])
    index = 1
    while queue:
        node = queue.popleft()
        if values[index] != "null":
            node.left = TreeNode(int(values[index]))
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] != "null":
            node.right = TreeNode(int(values[index]))
            queue.append(node.right)
        index += 1
    return root

#       Test Cases

def print_serialization(tree):
    return serialize(tree.root)

def test_serialize_deserialize():
    # Test Case 1: Normal binary tree
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    serialized1 = serialize(tree1.root)
    deserialized1 = deserialize(serialized1)
    print("Original 1:", serialized1)
    print("After Deserialization:", serialize(deserialized1))

    # Test Case 2: Empty tree
    tree2 = BinaryTree()
    serialized2 = serialize(tree2.root)
    deserialized2 = deserialize(serialized2)
    print("Original 2:", serialized2)
    print("After Deserialization:", serialize(deserialized2))

    # Test Case 3: Single node tree
    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])
    serialized3 = serialize(tree3.root)
    deserialized3 = deserialize(serialized3)
    print("Original 3:", serialized3)
    print("After Deserialization:", serialize(deserialized3))

    # Test Case 4: Left-skewed tree
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    serialized4 = serialize(tree4.root)
    deserialized4 = deserialize(serialized4)
    print("Original 4:", serialized4)
    print("After Deserialization:", serialize(deserialized4))

    # Test Case 5: Right-skewed tree
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    serialized5 = serialize(tree5.root)
    deserialized5 = deserialize(serialized5)
    print("Original 5:", serialized5)
    print("After Deserialization:", serialize(deserialized5))

test_serialize_deserialize()
