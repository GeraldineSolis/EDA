class Node:
    def __init__(self, value):
        self.value = value          # Stores the node’s value
        self.left = None            # Left child
        self.right = None           # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None            # Initialize an empty BST

    def insert(self, value):
        def _insert(node, value):
            if not node: return Node(value)      # Create a new node if we reach a leaf
            if value < node.value:
                node.left = _insert(node.left, value)   # Insert into the left subtree
            else:
                node.right = _insert(node.right, value) # Insert into the right subtree
            return node
        self.root = _insert(self.root, value)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)         # Visit left subtree
                result.append(node.value)   # Visit current node
                _inorder(node.right)        # Visit right subtree
        _inorder(self.root)
        return result                       # Return sorted list of values

def build_balanced_bst(sorted_array):
    if not sorted_array:
        return None                         # Base case: empty array
    mid = len(sorted_array) // 2
    node = Node(sorted_array[mid])         # Choose middle as root
    node.left = build_balanced_bst(sorted_array[:mid])       # Build left subtree recursively
    node.right = build_balanced_bst(sorted_array[mid+1:])    # Build right subtree recursively
    return node

def balance_bst(bst):
    sorted_nodes = bst.inorder()           # Get inorder list of nodes
    balanced_root = build_balanced_bst(sorted_nodes)   # Build balanced BST
    balanced_tree = BinarySearchTree()
    balanced_tree.root = balanced_root
    return balanced_tree                   # Return the balanced BST


#           Test Cases

def print_inorder(bst):
    print(bst.inorder())

def test_balance_bst():
    # Test Case 1: Already balanced tree
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    balanced1 = balance_bst(bst1)
    print("Balanced1:", balanced1.inorder())

    # Test Case 2: Right-skewed tree
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    balanced2 = balance_bst(bst2)
    print("Balanced2:", balanced2.inorder())

    # Test Case 3: Left-skewed tree
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)
    balanced3 = balance_bst(bst3)
    print("Balanced3:", balanced3.inorder())

    # Test Case 4: Empty tree
    bst4 = BinarySearchTree()
    balanced4 = balance_bst(bst4)
    print("Balanced4:", balanced4.inorder())

    # Test Case 5: Single node tree
    bst5 = BinarySearchTree()
    bst5.insert(42)
    balanced5 = balance_bst(bst5)
    print("Balanced5:", balanced5.inorder())

test_balance_bst()
