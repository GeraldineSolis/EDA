class Node:
    def __init__(self, val):
        self.val = val  # Initialize the value of the node (operator or number)
        self.left = None  # Initialize the left child (to be assigned later)
        self.right = None  # Initialize the right child (to be assigned later)

def evaluate_expression_tree(root):
    """Evaluate an expression tree and return the result."""
    
    # Base case: if the node is None, return 0
    if root is None:
        return 0  # Empty tree, though this edge case won't be necessary in normal cases
    
    # If it's a leaf node (no children), it's a number node
    if root.left is None and root.right is None:
        return int(root.val)  # Convert the value of the node to an integer and return it

    # Recursively evaluate the left and right subtrees
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    """Depending on the operator at the current node, apply the operation to the 
    results of the left and right children"""
    if root.val == '+':
        return left_val + right_val  # Perform addition
    elif root.val == '-':
        return left_val - right_val  # Perform subtraction
    elif root.val == '*':
        return left_val * right_val  # Perform multiplication
    elif root.val == '/':
        # Handle division carefully (integer division)
        if right_val == 0:
            raise ValueError("Division by zero is not allowed")  # Handle division by zero error
        return left_val // right_val  # Perform integer division

# ✅ Test cases
# Test 1: Simple addition
# Result: 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)  # ➕ Basic addition

# Test 2: Multiplication
# Result: 20
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)  # ✖️ Multiplication

# Test 3: Combined operations
# Result: 14
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)  # 🔢 Combined operations

# Test 4: Division
# Result: 2
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)  # ➗ Division

# Test 5: Complex tree
# Result: 15
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)  # 🧮 Complex calculation