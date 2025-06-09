class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, value):
        # Add the new value at the end of the heap list
        self.heap.append(value)
        # Restore heap property by moving the new element up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # While index is not root (index > 0)
        while index > 0:
            # Find parent index
            parent_index = (index - 1) // 2
            # If current node is smaller than parent, swap them
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Move index up to parent's position to continue heapify
                index = parent_index
            else:
                # Heap property satisfied, stop
                break

#Test cases 
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5)
    print("🍀 Test 1:", h.heap == [5])
    h.insert(3)
    print("🍀 Test 2:", h.heap == [3, 5])
    h.insert(4)
    print("🍀 Test 3:", h.heap == [3, 5, 4])
    h.insert(1)
    print("🍀 Test 4:", h.heap == [1, 3, 4, 5])

    # Heap property check: parent <= children
    valid = True
    for i in range(len(h.heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(h.heap) and h.heap[i] > h.heap[left]:
            valid = False
        if right < len(h.heap) and h.heap[i] > h.heap[right]:
            valid = False
    print("🍀 Test 5:", valid)

test_min_heap_insert()
