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

def consulta_rango(raiz, min_val, max_val):
    """Encuentra todos los valores en el BST dentro del rango dado"""
    resultado = []

    def inorden(nodo):
        if not nodo:
            return
        if nodo.valor > min_val:
            inorden(nodo.izquierda)
        if min_val <= nodo.valor <= max_val:
            resultado.append(nodo.valor)
        if nodo.valor < max_val:
            inorden(nodo.derecha)

    inorden(raiz)
    return resultado

# 🧪 Pruebas
print(consulta_rango(construir_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])
print(consulta_rango(construir_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])
print(consulta_rango(construir_bst([20, 10, 30]), 1, 5) == [])
print(consulta_rango(construir_bst([15]), 10, 20) == [15])
print(consulta_rango(construir_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])
