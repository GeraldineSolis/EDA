class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def delete_min(self):
        # If heap is empty, return None
        if not self.heap:
            return None

        # Save min value from root
        min_val = self.heap[0]

        # Replace root with last element
        last_val = self.heap.pop()  # Remove last element

        if self.heap:
            self.heap[0] = last_val
            # Restore heap property by pushing root down
            self._heapify_down(0)

        return min_val

    def _heapify_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Check left child
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check right child
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If the smallest is not the current index, swap and continue
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                # Heap property restored
                break

#   Test Cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap = [1]
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]
    min_val = min(h.heap)
    print("🧹 Test 5:", h.delete_min() == min_val)

test_min_heap_delete_min()
