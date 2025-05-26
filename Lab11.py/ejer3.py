class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    """
    Check if a binary tree is a valid Binary Search Tree (BST).
    Uses recursive validation with min/max bounds.
    """
    def helper(node, low, high):
        # An empty node is valid
        if node is None:
            return True
        
        # Current node must be strictly between low and high
        if not (low < node.val < high):
            return False
        
        # Left subtree must be < node.val
        if not helper(node.left, low, node.val):
            return False
        
        # Right subtree must be > node.val
        if not helper(node.right, node.val, high):
            return False
        
        return True
    
    return helper(root, float('-inf'), float('inf'))

# Helper function to build a binary tree from a list (level order)
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Build invalid BST with left violation
def build_invalid_tree1():
    #      5
    #     / \
    #    6   7  <-- 6 > 5 invalid left child
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    return root

# Build invalid BST with right violation
def build_invalid_tree2():
    #      5
    #     / \
    #    3   4  <-- 4 < 5 invalid right child
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root

# ------------------ Test cases ------------------

# Test 1: Valid BST
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)  # True

# Test 2: Invalid BST - left violation
print(is_valid_bst(build_invalid_tree1()) == False)  # False

# Test 3: Invalid BST - right violation
print(is_valid_bst(build_invalid_tree2()) == False)  # False

# Test 4: Single node (valid BST)
print(is_valid_bst(build_tree([42])) == True)  # True

# Test 5: Empty tree (valid BST)
print(is_valid_bst(None) == True)  # True
