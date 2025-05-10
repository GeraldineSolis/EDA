class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root):
    def check_height(node):
        # Si el nodo es None, su altura es 0
        if node is None:
            return 0
       
        # Calcular la altura del subárbol izquierdo
        left_height = check_height(node.left)
        if left_height == -1:  # Si el subárbol izquierdo no es balanceado
            return -1
       
        # Calcular la altura del subárbol derecho
        right_height = check_height(node.right)
        if right_height == -1:  # Si el subárbol derecho no es balanceado
            return -1
       
        # Si la diferencia de altura es mayor que 1, el árbol no está balanceado
        if abs(left_height - right_height) > 1:
            return -1
       
        # Retornar la altura del nodo actual
        return 1 + max(left_height, right_height)
   
    # Iniciar el chequeo de balance a partir de la raíz
    return check_height(root) != -1


def test_is_balanced():
    # Test Case 1: Árbol balanceado
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
   
    resultado = is_balanced(balanced)
    print(f"Prueba 1: Árbol balanceado - Esperado: True, Obtenido: {resultado}")
   
    # Test Case 2: Árbol vacío (trivially balanced)
    empty_tree = None
    resultado = is_balanced(empty_tree)
    print(f"Prueba 2: Árbol vacío - Esperado: True, Obtenido: {resultado}")
   
    # Test Case 3: Árbol con un solo nodo (trivially balanced)
    single_node = TreeNode(1)
    resultado = is_balanced(single_node)
    print(f"Prueba 3: Árbol con un solo nodo - Esperado: True, Obtenido: {resultado}")
   
    # Test Case 4: Árbol desbalanceado - Pesado a la izquierda
    unbalanced_left = TreeNode(1)
    unbalanced_left.left = TreeNode(2)
    unbalanced_left.left.left = TreeNode(3)
    unbalanced_left.left.left.left = TreeNode(4)
    resultado = is_balanced(unbalanced_left)
    print(f"Prueba 4: Árbol desbalanceado a la izquierda - Esperado: False, Obtenido: {resultado}")
   
    # Test Case 5: Árbol justo balanceado (caso límite)
    edge_balanced = TreeNode(1)
    edge_balanced.left = TreeNode(2)
    edge_balanced.right = TreeNode(3)
    edge_balanced.left.left = TreeNode(4)
    edge_balanced.left.right = TreeNode(5)
    edge_balanced.left.left.left = TreeNode(6)
    resultado = is_balanced(edge_balanced)
    print(f"Prueba 5: Árbol justo balanceado - Esperado: True, Obtenido: {resultado}")


# Ejecutar los casos de prueba
test_is_balanced()
