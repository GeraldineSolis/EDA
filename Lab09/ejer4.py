class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def find_leaves(root):
    """Encuentra todas las hojitas del árbol 🍃"""
    if root is None:
        return []

    if not root.children:
        return [root.value]

    leaves = []
    for child in root.children:
        leaves.extend(find_leaves(child))
    return leaves

def test_find_leaves():
    print("🌟 Test 1: Árbol vacío")
    test1_root = None
    print("Resultado:", find_leaves(test1_root))  # ➜ []

    print("\n🌟 Test 2: Solo un nodo (raíz es hoja)")
    test2_root = GenericTreeNode('A')
    print("Resultado:", find_leaves(test2_root))  # ➜ ['A']

    print("\n🌟 Test 3: Árbol lineal A → B → C")
    test3_root = GenericTreeNode('A')
    test3_b = GenericTreeNode('B')
    test3_c = GenericTreeNode('C')
    test3_root.add_child(test3_b)
    test3_b.add_child(test3_c)
    print("Resultado:", find_leaves(test3_root))  # ➜ ['C']

    print("\n🌟 Test 4: Árbol balanceado")
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
    print("Resultado:", find_leaves(test4_root))  # ➜ ['E', 'F', 'G', 'C', 'H']

    print("\n🌟 Test 5: Árbol más complicado")
    test5_root = GenericTreeNode('A')
    test5_b = GenericTreeNode('B')
    test5_c = GenericTreeNode('C')
    test5_d = GenericTreeNode('D')
    test5_e = GenericTreeNode('E')
    test5_f = GenericTreeNode('F')
    test5_g = GenericTreeNode('G')
    test5_h = GenericTreeNode('H')
    test5_i = GenericTreeNode('I')
    test5_j = GenericTreeNode('J')
    test5_k = GenericTreeNode('K')
    test5_root.add_child(test5_b)
    test5_root.add_child(test5_c)
    test5_root.add_child(test5_d)
    test5_b.add_child(test5_e)
    test5_b.add_child(test5_f)
    test5_d.add_child(test5_g)
    test5_e.add_child(test5_h)
    test5_f.add_child(test5_i)
    test5_f.add_child(test5_j)
    test5_f.add_child(test5_k)
    print("Resultado:", find_leaves(test5_root))  # ➜ ['H', 'I', 'J', 'K', 'C', 'G']

# ¡Vamos a correr los tests! 🧪
test_find_leaves()
