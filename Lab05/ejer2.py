from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def recorrido_niveles(raiz):
    if not raiz:
        return []

    resultado = []
    cola = deque()
    cola.append(raiz)

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izq:
            cola.append(nodo.izq)
        if nodo.der:
            cola.append(nodo.der)

    return resultado
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.der = Nodo(6)

resultado = recorrido_niveles(raiz)
print("Recorrido por niveles:", resultado)  # 👉 [1, 2, 3, 4, 5, 6]
