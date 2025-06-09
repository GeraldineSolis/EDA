class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # default height for new node

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def is_avl_balanced(self, root):
        """📏 Check if tree is AVL-balanced"""

        def check(node):
            # Base case: empty subtree is balanced, height 0
            if not node:
                return 0

            # Recursively check left subtree height
            left_height = check(node.left)
            if left_height == -1:
                return -1  # Left subtree not balanced, propagate failure

            # Recursively check right subtree height
            right_height = check(node.right)
            if right_height == -1:
                return -1  # Right subtree not balanced

            # Check balance factor of current node
            if abs(left_height - right_height) > 1:
                return -1  # Current node unbalanced

            # Check if node height matches max height of subtrees + 1
            expected_height = max(left_height, right_height) + 1
            if node.height != expected_height:
                return -1  # Height mismatch indicates invalid AVL height info

            # Return height if balanced
            return expected_height

        # If check returns -1, tree is not balanced AVL, else True
        return check(root) != -1


    # Minimal insert method to build AVL tree for testing
    def insert(self, root, key):
        # Normal BST insert
        if not root:
            return AVLNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # For this challenge, no rotations needed (just balance check)
        return root

#   Test cases
def test_is_avl_balanced():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # ✅

    # Simulate imbalance manually
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ⚠️

    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)  # 🌱
    # More cases in complex structures...

# 🚀 Run tests
test_is_avl_balanced()
