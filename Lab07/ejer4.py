from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    # Si el árbol está vacío, retornamos una lista vacía
    if root is None:
        return []
   
    result = []
    queue = deque([root])  # Usamos deque para simular una cola
   
    while queue:
        node = queue.popleft()  # Extraemos el nodo al frente de la cola
        result.append(node.value)  # Agregamos su valor al resultado
       
        # Agregamos los hijos izquierdo y derecho a la cola si existen
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
   
    return result


def test_level_order_traversal():
    # Test Case 1: Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
   
    resultado = level_order_traversal(root)
    print(f"Prueba 1: Árbol normal - Esperado: [1, 2, 3, 4, 5, 6], Obtenido: {resultado}")
   
    # Test Case 2: Árbol vacío
    empty_tree = None
    resultado = level_order_traversal(empty_tree)
    print(f"Prueba 2: Árbol vacío - Esperado: [], Obtenido: {resultado}")
   
    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    resultado = level_order_traversal(single_node)
    print(f"Prueba 3: Árbol con un solo nodo - Esperado: [1], Obtenido: {resultado}")
   
    # Test Case 4: Árbol sesgado a la izquierda
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    resultado = level_order_traversal(left_skewed)
    print(f"Prueba 4: Árbol sesgado a la izquierda - Esperado: [1, 2, 3, 4], Obtenido: {resultado}")
   
    # Test Case 5: Árbol sesgado a la derecha
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    resultado = level_order_traversal(right_skewed)
    print(f"Prueba 5: Árbol sesgado a la derecha - Esperado: [1, 2, 3, 4], Obtenido: {resultado}")


# Ejecutar los casos de prueba
test_level_order_traversal()
