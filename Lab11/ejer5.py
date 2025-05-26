class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left  # Will act as prev in DLL
        self.right = right  # Will act as next in DLL

def build_bst(nums):
    """Helper to build BST from list of numbers."""
    if not nums:
        return None
    root = None
    for num in nums:
        root = insert_into_bst(root, num)
    return root

def insert_into_bst(root, val):
    """Insert val into BST recursively."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def build_degenerate_bst(nums):
    """Helper to build a degenerate BST (like linked list) 
    where every node has only right child."""
    if not nums:
        return None
    root = TreeNode(nums[0])
    current = root
    for val in nums[1:]:
        current.right = TreeNode(val)
        current = current.right
    return root

def bst_to_dll(root):
    """Convert BST to sorted circular doubly linked list in-place."""
    if root is None:
        return None

    first, last = None, None

    def inorder(node):
        nonlocal first, last
        if node is None:
            return

        # Traverse left subtree
        inorder(node.left)

        # Link previous node (last) with current node
        if last:
            last.right, node.left = node, last  # last.next = current node, current.prev = last node
        else:
            first = node  # First node found (smallest)
        last = node  # Update last to current node
        # Traverse right subtree
        inorder(node.right)

    inorder(root)

    # Close the circular DLL by connecting first and last nodes
    last.right = first
    first.left = last

    return first

def validate_circular_dll(head, expected_vals):
    """Validate if the circular doubly linked list has nodes with expected 
    values in order."""
    if not head and not expected_vals:
        return True  # Both empty

    if not head or not expected_vals:
        return False  # One empty, one not

    n = len(expected_vals)
    curr = head
    result = []

    # Traverse forward for n nodes
    for _ in range(n):
        result.append(curr.val)
        curr = curr.right

    if result != expected_vals:
        return False

    # Verify circularity by checking if after n moves we are back at head
    if curr != head:
        return False

    # Verify backward links
    curr = head.left  # Should be tail
    for val in reversed(expected_vals):
        if curr.val != val:
            return False
        curr = curr.left

    return True

# Test 1: Simple BST
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Simple conversiSon

# Test 2: Larger BST
head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Complex conversion

# Test 3: Single node
head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Single node

# Test 4: Degenerate BST (like linked list)
head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate case

# Test 5: Empty tree
head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Empty tree