# Cliente simple
class Cliente:
    def __init__(self, nombre, articulos):
        self.nombre = nombre
        self.articulos = articulos

# Caja sencilla con velocidad
class Caja:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.cola = []

    def agregar_cliente(self, cliente):
        self.cola.append(cliente)

    def atender(self):
        if self.cola:
            cliente = self.cola[0]
            cliente.articulos -= self.velocidad
            print(f" Atendiendo a {cliente.nombre}, le quedan {max(cliente.articulos, 0)} artículos")
            if cliente.articulos <= 0:
                print(f"{cliente.nombre} ya terminó")
                self.cola.pop(0)

# Supermercado que reparte clientes
class Supermercado:
    def __init__(self, cajas):
        self.cajas = cajas

    def nuevo_cliente(self, cliente):
        # Buscar la caja con menos clientes
        caja_mas_corta = min(self.cajas, key=lambda c: len(c.cola))
        caja_mas_corta.agregar_cliente(cliente)
        print(f" {cliente.nombre} va a una caja con velocidad {caja_mas_corta.velocidad}")

    def pasar_minuto(self):
        print("\n Pasa 1 minuto...")
        for caja in self.cajas:
            caja.atender()

# Crear dos cajas: una lenta (1) y una rápida (2)
caja1 = Caja(1)
caja2 = Caja(2)

mercado = Supermercado([caja1, caja2])

# Llegan clientes
mercado.nuevo_cliente(Cliente("Ana", 4))
mercado.nuevo_cliente(Cliente("Beto", 3))
mercado.nuevo_cliente(Cliente("Cami", 2))
mercado.nuevo_cliente(Cliente("Dani", 1))

# Simular 5 minutos
for i in range(5):
    mercado.pasar_minuto()
