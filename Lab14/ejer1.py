test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # Inicializa la lista vacía para almacenar los elementos del heap
        self.heap = []

    def is_empty(self):
        # Retorna True si la lista del heap está vacía
        return len(self.heap) == 0

    def size(self):
        # Retorna la cantidad de elementos en el heap
        return len(self.heap)

    def peek(self):
        # Retorna el elemento mínimo (el primero en la lista)
        # Si el heap está vacío, retorna None
        if self.is_empty():
            return None
        return self.heap[0]

# Casos de prueba (Tests)
def test_1_1():
    # 1.1.1 Empty heap initialization
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)
    
    # 1.1.2 Size tracking
    heap.heap = [1, 3, 2]  # Simulación de elementos añadidos
    record_test("1.1.2 Size tracking", heap.size() == 3)
    
    # 1.1.3 Peek functionality
    record_test("1.1.3 Peek functionality", heap.peek() == 1)
    
    # 1.1.4 Empty heap edge case
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)
    
    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

# Ejecutar pruebas
test_1_1()

# Resumen de pruebas
for r in test_results:
    print(r)
