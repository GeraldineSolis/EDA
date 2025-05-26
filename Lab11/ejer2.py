class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_bst(valores):
    """Construye un BST a partir de una lista de valores"""
    if not valores:
        return None

    raiz = Nodo(valores[0])
    for val in valores[1:]:
        insertar_en_bst(raiz, val)
    return raiz

def insertar_en_bst(raiz, valor):
    if valor < raiz.valor:
        if raiz.izquierda:
            insertar_en_bst(raiz.izquierda, valor)
        else:
            raiz.izquierda = Nodo(valor)
    else:
        if raiz.derecha:
            insertar_en_bst(raiz.derecha, valor)
        else:
            raiz.derecha = Nodo(valor)

def encontrar_lca(raiz, val1, val2):
    """Encuentra el ancestro común más bajo de dos valores en BST"""
    nodo = raiz
    while nodo:
        if val1 < nodo.valor and val2 < nodo.valor:
            nodo = nodo.izquierda
        elif val1 > nodo.valor and val2 > nodo.valor:
            nodo = nodo.derecha
        else:
            return nodo.valor
    return None  # Por si no se encuentra, aunque no debería ocurrir en BST válido

# 🧪 Pruebas
print(encontrar_lca(construir_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # Root as LCA
print(encontrar_lca(construir_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # Subtree LCA
print(encontrar_lca(construir_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # Ancestor relationship
print(encontrar_lca(construir_bst([5, 3, 7]), 5, 5) == 5)                    # Same node
print(encontrar_lca(construir_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)        # Leaf nodes
