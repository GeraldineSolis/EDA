test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear  = None
        self._size = 0

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def enqueue(self, item):
        """Add item to rear."""
        node = Node(item)
        
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = self.rear = node
        self._size += 1

    def dequeue(self):
        """Remove and return front item or None."""
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next

        if not self.front:
            self.rear = None
        
        self._size -= 1
        return data

    def size(self):
        """Return number of elements."""
        return self._size

def test_o5_2():
    q = LinkedQueue()
    record_test("o5.2.1 empty", q.is_empty() is True and q.size() == 0)

    q.enqueue("a"); q.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        q.is_empty() is False and q.size() == 2 and q.dequeue() == "a")

    q.dequeue()
    record_test("o5.2.3 drained",
        q.is_empty() is True and q.size() == 0)

    old = q.size()
    record_test("o5.2.4 invalid dequeue",
        q.dequeue() is None and q.size() == old)

    record_test("o5.2.5 return types",
        isinstance(q.is_empty(), bool)
        and isinstance(q.size(), int)
        and isinstance(q.dequeue(), (int,str,type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for r in test_results:
    print(r)
