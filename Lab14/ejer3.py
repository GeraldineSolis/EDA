test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []
    
    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Restore the heap property by bubbling the new value up
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        # Bubble the element at index up until heap property is restored
        while index > 0:
            parent_idx = self._parent_index(index)
            if self.heap[index] < self.heap[parent_idx]:
                # Swap if current value is less than parent
                self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                index = parent_idx  # Move up to parent index
            else:
                break  # Heap property satisfied

    def _parent_index(self, index):
        # Return parent index, or -1 if root
        return (index - 1) // 2 if index > 0 else -1
    
    def size(self):
        # Return number of elements in heap
        return len(self.heap)
    
    def peek(self):
        # Return min element (root), or None if empty
        return self.heap[0] if self.heap else None

# Test Suite for Challenge 3
def test_1_3():
    heap = MinHeap()
    
    # 1.3.1 Single element insertion
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])
    
    # 1.3.2 Multiple insertions
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)
    
    # 1.3.3 Minimum tracking
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)
    
    # 1.3.4 Heap property validation
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] <= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)
    
    # 1.3.5 Size consistency
    record_test("1.3.5 Size consistency", heap.size() == 4)

# Run tests
test_1_3()

# Summary
for r in test_results:
    print(r)
