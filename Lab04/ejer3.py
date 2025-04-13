class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)

        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        
    def pop(self):
        if self.stack:
            popped = self.stack.pop()

            if popped == self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        return None
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(1)
min_stack.pop()

print(min_stack.top())
print(min_stack.getMin())