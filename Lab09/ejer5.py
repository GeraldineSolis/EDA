class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def simplify_expression(node):
    if node is None:
        return None

    node.left = simplify_expression(node.left)
    node.right = simplify_expression(node.right)

    if node.value in {'+', '-', '*', '/'} and node.left and node.right:
        if is_number(node.left.value) and is_number(node.right.value):
            left_val = int(node.left.value)
            right_val = int(node.right.value)
            if node.value == '+':
                result = left_val + right_val
            elif node.value == '-':
                result = left_val - right_val
            elif node.value == '*':
                result = left_val * right_val
            elif node.value == '/':
                result = left_val // right_val if right_val != 0 else 0
            return ExpressionNode(str(result))
    return node

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def print_expression_tree(node):
    """Imprime el árbol como una expresión en orden."""
    if node is None:
        return ""
    if node.left is None and node.right is None:
        return node.value
    left = print_expression_tree(node.left)
    right = print_expression_tree(node.right)
    return f"({left} {node.value} {right})"

def test_simplify_expression():
    print("🌟 Test Case 1: (2 + 3) * 4")
    test1_root = ExpressionNode('*')
    test1_add = ExpressionNode('+')
    test1_2 = ExpressionNode('2')
    test1_3 = ExpressionNode('3')
    test1_4 = ExpressionNode('4')
    test1_add.left = test1_2
    test1_add.right = test1_3
    test1_root.left = test1_add
    test1_root.right = test1_4
    simplified1 = simplify_expression(test1_root)
    print("Resultado:", print_expression_tree(simplified1))  # ➜ 20

    print("\n🌟 Test Case 2: (2 + 3) * x")
    test2_root = ExpressionNode('*')
    test2_add = ExpressionNode('+')
    test2_2 = ExpressionNode('2')
    test2_3 = ExpressionNode('3')
    test2_x = ExpressionNode('x')
    test2_add.left = test2_2
    test2_add.right = test2_3
    test2_root.left = test2_add
    test2_root.right = test2_x
    simplified2 = simplify_expression(test2_root)
    print("Resultado:", print_expression_tree(simplified2))  # ➜ (5 * x)

    print("\n🌟 Test Case 3: (x + y) * z")
    test3_root = ExpressionNode('*')
    test3_add = ExpressionNode('+')
    test3_x = ExpressionNode('x')
    test3_y = ExpressionNode('y')
    test3_z = ExpressionNode('z')
    test3_add.left = test3_x
    test3_add.right = test3_y
    test3_root.left = test3_add
    test3_root.right = test3_z
    simplified3 = simplify_expression(test3_root)
    print("Resultado:", print_expression_tree(simplified3))  # ➜ ((x + y) * z)

    print("\n🌟 Test Case 4: ((2 * 3) + (4 - 1)) * 5")
    test4_root = ExpressionNode('*')
    test4_add = ExpressionNode('+')
    test4_mult = ExpressionNode('*')
    test4_sub = ExpressionNode('-')
    test4_2 = ExpressionNode('2')
    test4_3 = ExpressionNode('3')
    test4_4 = ExpressionNode('4')
    test4_1 = ExpressionNode('1')
    test4_5 = ExpressionNode('5')
    test4_mult.left = test4_2
    test4_mult.right = test4_3
    test4_sub.left = test4_4
    test4_sub.right = test4_1
    test4_add.left = test4_mult
    test4_add.right = test4_sub
    test4_root.left = test4_add
    test4_root.right = test4_5
    simplified4 = simplify_expression(test4_root)
    print("Resultado:", print_expression_tree(simplified4))  # ➜ 45

    print("\n🌟 Test Case 5: (x + 5) * (3 + 2)")
    test5_root = ExpressionNode('*')
    test5_add1 = ExpressionNode('+')
    test5_add2 = ExpressionNode('+')
    test5_x = ExpressionNode('x')
    test5_5a = ExpressionNode('5')
    test5_3 = ExpressionNode('3')
    test5_2 = ExpressionNode('2')
    test5_add1.left = test5_x
    test5_add1.right = test5_5a
    test5_add2.left = test5_3
    test5_add2.right = test5_2
    test5_root.left = test5_add1
    test5_root.right = test5_add2
    simplified5 = simplify_expression(test5_root)
    print("Resultado:", print_expression_tree(simplified5))  # ➜ ((x + 5) * 5)

# ¡Ejecutamos los tests!
test_simplify_expression()
