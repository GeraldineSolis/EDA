class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def tree_height(root):
    """Encuentra la altura del árbol 🌲📏"""
    if root is None:
        return 0
    if not root.children:
        return 1
    return 1 + max(tree_height(child) for child in root.children)

def test_tree_height():
    print("🌱 Test 1: Árbol vacío")
    test1_root = None
    print("Altura:", tree_height(test1_root))  # ➜ 0

    print("\n🌱 Test 2: Solo un nodo")
    test2_root = GenericTreeNode('A')
    print("Altura:", tree_height(test2_root))  # ➜ 1

    print("\n🌱 Test 3: Árbol lineal A → B → C → D")
    test3_root = GenericTreeNode('A')
    test3_b = GenericTreeNode('B')
    test3_c = GenericTreeNode('C')
    test3_d = GenericTreeNode('D')
    test3_root.add_child(test3_b)
    test3_b.add_child(test3_c)
    test3_c.add_child(test3_d)
    print("Altura:", tree_height(test3_root))  # ➜ 4

    print("\n🌱 Test 4: Árbol balanceado")
    test4_root = GenericTreeNode('A')
    test4_b = GenericTreeNode('B')
    test4_c = GenericTreeNode('C')
    test4_d = GenericTreeNode('D')
    test4_e = GenericTreeNode('E')
    test4_f = GenericTreeNode('F')
    test4_g = GenericTreeNode('G')
    test4_h = GenericTreeNode('H')
    test4_root.add_child(test4_b)
    test4_root.add_child(test4_c)
    test4_root.add_child(test4_d)
    test4_b.add_child(test4_e)
    test4_b.add_child(test4_f)
    test4_b.add_child(test4_g)
    test4_d.add_child(test4_h)
    print("Altura:", tree_height(test4_root))  # ➜ 3

    print("\n🌱 Test 5: Árbol no balanceado")
    test5_root = GenericTreeNode('A')
    test5_b = GenericTreeNode('B')
    test5_c = GenericTreeNode('C')
    test5_d = GenericTreeNode('D')
    test5_e = GenericTreeNode('E')
    test5_f = GenericTreeNode('F')
    test5_g = GenericTreeNode('G')
    test5_root.add_child(test5_b)
    test5_root.add_child(test5_c)
    test5_b.add_child(test5_d)
    test5_c.add_child(test5_e)
    test5_d.add_child(test5_f)
    test5_e.add_child(test5_g)
    print("Altura:", tree_height(test5_root))  # ➜ 4

# ¡Probamos todos los test! 🧪
test_tree_height()
