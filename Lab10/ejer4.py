class Node:
    def __init__(self, val):
        self.val = val  # Initialize the node with a value (operator or operand)
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def inorder_traversal(root):
    """Perform inorder traversal (left, root, right)"""
    if root is None:
        return []  # If the node is None, return an empty list (base case)
    # Recursively traverse the left subtree, visit the node, and then the right subtree
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def preorder_traversal(root):
    """Perform preorder traversal (root, left, right)"""
    if root is None:
        return []  # If the node is None, return an empty list (base case)
    # Visit the node first, then recursively traverse the left and right subtrees
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root):
    """Perform postorder traversal (left, right, root)"""
    if root is None:
        return []  # If the node is None, return an empty list (base case)
    # Recursively traverse the left and right subtrees, then visit the node
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

# ✅ Test cases
# Test 1: Simple expression tree
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(inorder_traversal(node1) == ['2', '+', '3'])  # 📝 Infix notation
print(preorder_traversal(node1) == ['+', '2', '3'])  # 📝 Prefix notation
print(postorder_traversal(node1) == ['2', '3', '+'])  # 📝 Postfix notation

# Test 2: More complex tree
node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])  # 📝 Infix with precedence
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])  # 📝 Prefix order
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])  # 📝 Postfix order

# Test 3: Single node tree
# Tree: X
node3 = Node('X')
print(inorder_traversal(node3) == ['X'])  # 🌱 Single node inorder
print(preorder_traversal(node3) == ['X'])  # 🌱 Single node preorder
print(postorder_traversal(node3) == ['X'])  # 🌱 Single node postorder

# Test 4: Empty tree
# Tree: None
print(inorder_traversal(None) == [])  # 📭 Empty tree inorder
print(preorder_traversal(None) == [])  # 📭 Empty tree preorder
print(postorder_traversal(None) == [])  # 📭 Empty tree postorder

# Test 5: Complex nested tree
node5 = Node('/')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('a')
node5.left.right = Node('b')
node5.right.left = Node('c')
node5.right.right = Node('d')
print(inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'])  # 🧮 Complex inorder
print(preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'])  # 🧮 Complex preorder
print(postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'])  # 🧮 Complex postorder