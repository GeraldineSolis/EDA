class Node:
    def __init__(self, value):
        self.value = value  # Store the value (can be an operator or operand)
        self.left = None  # Left child
        self.right = None  # Right child

def simplify_expression_tree(root):
    """Simplify the expression tree by evaluating constant subtrees."""
    # Base case: if the node is None, return None
    if root is None:
        return None

    # If the node is a leaf (a number or variable), just return the node
    if root.left is None and root.right is None:
        return root

    # Simplify the left and right children first (post-order traversal)
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # If both left and right are numbers, evaluate the expression
    if root.left and root.right and root.left.value.isdigit() and root.right.value.isdigit():
        left_value = int(root.left.value)
        right_value = int(root.right.value)

        # Apply the operator to the constants
        if root.value == '+':
            result = left_value + right_value
        elif root.value == '-':
            result = left_value - right_value
        elif root.value == '*':
            result = left_value * right_value
        elif root.value == '/':
            # Check for division by zero
            if right_value == 0:
                raise ValueError("Division by zero!")
            result = left_value // right_value  # Integer division
        
        # Replace the current node with a new node containing the result
        root.value = str(result)
        root.left = None
        root.right = None
    
    return root

# ✅ Test cases
# Test 1: All constants
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # 🔢 Full evaluation

# Test 2: Mixed variables and constants
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # 🔤 Variable preserved

# Test 3: Partial simplification
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # 📊 Subtree simplification

# Test 4: All variables
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # 🔤 No simplification

# Test 5: Complex nested simplification
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # 🧮 Mixed simplification
