class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_height(root):
    # Si el árbol es vacío, la altura es -1
    if root is None:
        return -1
    # Calcular la altura de los subárboles izquierdo y derecho
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
   
    # La altura del árbol es el máximo de los subárboles + 1
    return max(left_height, right_height) + 1


def test_tree_height():
    # Test Case 1: Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
   
    resultado = tree_height(root)
    print(f"Prueba 1: Árbol normal - Esperado: 2, Obtenido: {resultado}")
   
    # Test Case 2: Árbol vacío
    empty_tree = None
    resultado = tree_height(empty_tree)
    print(f"Prueba 2: Árbol vacío - Esperado: -1, Obtenido: {resultado}")
   
    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    resultado = tree_height(single_node)
    print(f"Prueba 3: Árbol con un solo nodo - Esperado: 0, Obtenido: {resultado}")
   
    # Test Case 4: Árbol sesgado a la izquierda
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    resultado = tree_height(left_skewed)
    print(f"Prueba 4: Árbol sesgado a la izquierda - Esperado: 3, Obtenido: {resultado}")
   
    # Test Case 5: Árbol binario perfecto
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    resultado = tree_height(perfect)
    print(f"Prueba 5: Árbol binario perfecto - Esperado: 2, Obtenido: {resultado}")


# Ejecutar los casos de prueba
test_tree_height()
