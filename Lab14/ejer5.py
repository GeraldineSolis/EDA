test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        # Añadimos el valor al final y "subimos" para mantener la propiedad MaxHeap
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete_max(self):
        # Eliminamos y retornamos el máximo (raíz)
        if not self.heap:
            return None  # Si heap está vacío
        
        max_value = self.heap[0]
        # Colocamos el último elemento en la raíz y "bajamos" para restaurar heap
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)
        return max_value
    
    def build_heap(self, array):
        # Construimos el heap desde un array dado en O(n)
        self.heap = array[:]
        # Empezamos en el último nodo padre y vamos hacia arriba heapificando
        start_index = (len(self.heap) // 2) - 1
        for i in range(start_index, -1, -1):
            self._heapify_down(i)
    
    def _heapify_up(self, index):
        # Subimos el nodo en index si es mayor que su padre para mantener MaxHeap
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
    
    def _heapify_down(self, index):
        # Bajamos el nodo en index si es menor que alguno de sus hijos para mantener MaxHeap
        n = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == index:
                break
            
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def test_1_5():
    heap = MaxHeap()
    
    # 1.5.1 MaxHeap insertion
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)
    
    # 1.5.2 MaxHeap deletion
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)
    
    # 1.5.3 Build heap from array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))
    
    # 1.5.4 Heap property verification
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)
    
    # 1.5.5 Empty array handling
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# Ejecutamos los tests
test_1_5()

# Imprimimos resultados
for r in test_results:
    print(r)
