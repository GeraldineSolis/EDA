class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_bst(nums):
    """Helper function to build a BST from a list of numbers."""
    if not nums:
        return None
    root = None
    for num in nums:
        root = insert_into_bst(root, num)
    return root

def insert_into_bst(root, val):
    """Helper function to insert a value into the BST."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def kth_smallest(root, k):
    """Find the kth smallest element in a BST using inorder traversal."""

    counter = {'count': 0}  # Dictionary to keep track of count during recursion
    result = {'value': None} # Dictionary to store the kth smallest value once found

    def inorder(node):
        # Base case: if node is None or kth element found, stop recursion
        if node is None or result['value'] is not None:
            return

        # Traverse left subtree first (smaller values)
        inorder(node.left)

        # Increment count when visiting a node
        counter['count'] += 1

        # If count matches k, record the node value as result
        if counter['count'] == k:
            result['value'] = node.val
            return

        # Traverse right subtree (larger values)
        inorder(node.right)

    # Start inorder traversal from root
    inorder(root)

    # Return the kth smallest element found
    return result['value']

# Test 1: kth smallest in balanced BST
# BST: [3, 1, 4, 2] -> sorted: [1, 2, 3, 4]
# k = 2
# Expected output: 2
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # True

# Test 2: First smallest (minimum)
# BST: [5, 3, 7, 2, 4, 6, 8]
# k = 1
# Expected output: 2
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # True

# Test 3: Last element (maximum)
# BST: [5, 3, 7, 2, 4, 6, 8]
# k = 7
# Expected output: 8
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # True

# Test 4: Middle element
# BST: [4, 2, 6, 1, 3, 5, 7]
# k = 4
# Expected output: 4
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # True

# Test 5: Single node tree
# BST: [10]
# k = 1
# Expected output: 10
print(kth_smallest(build_bst([10]), 1) == 10)  # True

