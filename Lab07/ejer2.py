class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_leaves(root):
    # Si el árbol está vacío, no hay hojas
    if root is None:
        return 0
    # Si el nodo no tiene hijos izquierdo ni derecho, es un nodo hoja
    if root.left is None and root.right is None:
        return 1
    # Recursivamente contar hojas en los subárboles izquierdo y derecho
    return count_leaves(root.left) + count_leaves(root.right)


def test_count_leaves():
    # Test Case 1: Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
   
    resultado = count_leaves(root)
    print(f"Prueba 1: Árbol normal - Esperado: 3, Obtenido: {resultado}")
   
    # Test Case 2: Árbol vacío
    empty_tree = None
    resultado = count_leaves(empty_tree)
    print(f"Prueba 2: Árbol vacío - Esperado: 0, Obtenido: {resultado}")
   
    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    resultado = count_leaves(single_node)
    print(f"Prueba 3: Árbol con un solo nodo - Esperado: 1, Obtenido: {resultado}")
   
    # Test Case 4: No hay nodos hoja en el primer nivel
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    resultado = count_leaves(no_leaves_at_first)
    print(f"Prueba 4: No hay nodos hoja en el primer nivel - Esperado: 2, Obtenido: {resultado}")
   
    # Test Case 5: Todos los nodos son hojas, excepto la raíz
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    resultado = count_leaves(all_leaves)
    print(f"Prueba 5: Todos los nodos son hojas, excepto la raíz - Esperado: 6, Obtenido: {resultado}")


# Ejecutar los casos de prueba
test_count_leaves()
