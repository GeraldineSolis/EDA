class TreeNode:
    def __init__(self, value):
        self.value = value  # Store the operator or operand
        self.left = None    # Left child
        self.right = None   # Right child

def infix_to_postfix(tokens):
    # Same as previous implementation
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operator_stack = []
    output = []

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # remove '('

    while operator_stack:
        output.append(operator_stack.pop())
    return output

def build_tree_from_infix(tokens):
    # First, convert infix expression to postfix
    postfix = infix_to_postfix(tokens)

    # Stack to build tree nodes
    stack = []

    # Process each token in postfix
    for token in postfix:
        if token.isnumeric():
            # Operand → create leaf node and push
            node = TreeNode(token)
            stack.append(node)
        else:
            # Operator → pop two nodes and create new tree node
            right = stack.pop()  # Right operand
            left = stack.pop()   # Left operand
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

    # Final node is the root of the tree
    return stack[0]

#       Test Cases 
def print_tree(root, indent=""):
    """Print tree structure with root at top"""
    if root is not None:
        print_tree(root.right, indent + "   ")
        print(f"{indent}{root.value}")
        print_tree(root.left, indent + "   ")

def test_build_tree_from_infix():
    """Test building expression tree from infix. 🌳"""

    test1_input = ['2', '+', '3']
    print("Test 1: ['2', '+', '3']")
    root1 = build_tree_from_infix(test1_input)
    print_tree(root1)
    print("\nExpected Tree:\n   +\n  / \\\n 2   3\n")

    test2_input = ['2', '+', '3', '*', '4']
    print("Test 2: ['2', '+', '3', '*', '4']")
    root2 = build_tree_from_infix(test2_input)
    print_tree(root2)
    print("\nExpected Tree:\n   +\n  / \\\n 2   *\n     / \\\n    3   4\n")

    test3_input = ['(', '2', '+', '3', ')', '*', '4']
    print("Test 3: ['(', '2', '+', '3', ')', '*', '4']")
    root3 = build_tree_from_infix(test3_input)
    print_tree(root3)
    print("\nExpected Tree:\n   *\n  / \\\n +   4\n/ \\\n2   3\n")

    test4_input = ['5', '*', '(', '3', '+', '2', ')', '-', '10']
    print("Test 4: ['5', '*', '(', '3', '+', '2', ')', '-', '10']")
    root4 = build_tree_from_infix(test4_input)
    print_tree(root4)
    print("\nExpected Tree:\n   -\n  / \\\n *   10\n/ \\\n5   +\n   / \\\n  3   2\n")

    test5_input = ['8', '/', '4', '/', '2']
    print("Test 5: ['8', '/', '4', '/', '2']")
    root5 = build_tree_from_infix(test5_input)
    print_tree(root5)
    print("\nExpected Tree:\n   /\n  / \\\n /   2\n/ \\\n8   4\n")

# Run the tests
test_build_tree_from_infix()
