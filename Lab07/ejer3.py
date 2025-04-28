class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mirror_tree(root):
    # Si el árbol es vacío, no hay nada que hacer
    if root is None:
        return None
    # Intercambiar los hijos izquierdo y derecho
    root.left, root.right = root.right, root.left
   
    # Llamar recursivamente para los subárboles izquierdo y derecho
    mirror_tree(root.left)
    mirror_tree(root.right)
   
    return root


def test_mirror_tree():
    # Test Case 1: Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
   
    mirrored_root = mirror_tree(root)
    print("Prueba 1: Árbol normal")
    print(f"Antes de espejar: Raíz -> {mirrored_root.value}, Izquierda -> {mirrored_root.left.value if mirrored_root.left else 'None'}, Derecha -> {mirrored_root.right.value if mirrored_root.right else 'None'}")
   
    # Test Case 2: Árbol vacío
    empty_tree = None
    mirrored_empty_tree = mirror_tree(empty_tree)
    print(f"Prueba 2: Árbol vacío - Esperado: None, Obtenido: {mirrored_empty_tree}")
   
    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    mirrored_single_node = mirror_tree(single_node)
    print(f"Prueba 3: Árbol con un solo nodo - Antes de espejar: Raíz -> {mirrored_single_node.value}, Izquierda -> {mirrored_single_node.left}, Derecha -> {mirrored_single_node.right}")
   
    # Test Case 4: Árbol con solo hijos a la izquierda
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    mirrored_left_only = mirror_tree(left_only)
    print(f"Prueba 4: Árbol con solo hijos a la izquierda")
    print(f"Raíz -> {mirrored_left_only.value}, Izquierda -> {mirrored_left_only.left.value if mirrored_left_only.left else 'None'}, Derecha -> {mirrored_left_only.right.value if mirrored_left_only.right else 'None'}")
   
    # Test Case 5: Árbol binario perfecto
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    mirrored_perfect = mirror_tree(perfect)
    print(f"Prueba 5: Árbol binario perfecto")
    print(f"Raíz -> {mirrored_perfect.value}, Izquierda -> {mirrored_perfect.left.value if mirrored_perfect.left else 'None'}, Derecha -> {mirrored_perfect.right.value if mirrored_perfect.right else 'None'}")
    print(f"Raíz izquierda -> {mirrored_perfect.left.value if mirrored_perfect.left else 'None'}, Izquierda -> {mirrored_perfect.left.left.value if mirrored_perfect.left.left else 'None'}, Derecha -> {mirrored_perfect.left.right.value if mirrored_perfect.left.right else 'None'}")


# Ejecutar los casos de prueba
test_mirror_tree()
