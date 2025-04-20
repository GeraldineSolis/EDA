class ColaConDosPilas:
    def __init__(self):
        self.pilaEntrada = []
        self.pilaSalida = []

    def encolar(self, valor):
        self.pilaEntrada.append(valor)

    def desencolar(self):
        if not self.pilaSalida:
            while self.pilaEntrada:
                self.pilaSalida.append(self.pilaEntrada.pop())
        if self.pilaSalida:
            return self.pilaSalida.pop()
        return None

    def frente(self):
        if not self.pilaSalida:
            while self.pilaEntrada:
                self.pilaSalida.append(self.pilaEntrada.pop())
        if self.pilaSalida:
            return self.pilaSalida[-1]
        return None

    def esta_vacia(self):
        return not self.pilaEntrada and not self.pilaSalida

    def tamano(self):
        return len(self.pilaEntrada) + len(self.pilaSalida)
cola = ColaConDosPilas()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Frente:", cola.frente())  # 👉 1
print("Desencolar:", cola.desencolar())  # 👉 1
print("Frente ahora:", cola.frente())  # 👉 2
print("Tamaño:", cola.tamano())  # 👉 2
print("¿Está vacía?", cola.esta_vacia())  # 👉 False
