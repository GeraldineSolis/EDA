from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Height of node starts at 1 for leaf nodes

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        # Step 1 - Perform normal BST insert
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If node is unbalanced, try the 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) node pointer
        return root

    def print_level_order(self, root):
        """📡 Level-order print with heights"""

        if not root:
            return  # Empty tree, print nothing

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)  # Number of nodes at current level
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                # Append string of node value and height
                level_nodes.append(f"{node.val}(h{node.height})")

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Print all nodes in the current level separated by commas
            print(", ".join(level_nodes))

#   Test Cases
def test_level_order_heights():
    avl = AVLTree()
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("🧪 Test 1-5: Expected output:")
    # 10(h3)
    # 5(h2), 15(h1)
    # 2(h1), 7(h1)SS
    avl.print_level_order(root)

# 🚀 Go!
test_level_order_heights()
