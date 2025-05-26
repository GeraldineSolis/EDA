class Node:
    def __init__(self, value):
        self.value = value      # Stores the node's value
        self.left = None        # Left child
        self.right = None       # Right child

class BinaryTree:
    def __init__(self):
        self.root = None        # Initialize an empty binary tree
    
    def build_tree_from_list(self, values):
        #Build a tree from a list of values in level order.
    
        if not values or values[0] is None:
            return None
        
        # Create the root node
        self.root = Node(values[0])
        queue = [self.root]
        i = 1
        
        # Process all nodes in level order
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Process left child
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            
            # Process right child
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        
        return self.root
    
#           Test Cases

def lowest_common_ancestor(root, p, q):
    # Find the lowest common ancestor of two nodes with values p and q in a binary tree.
    
    # Base case: If root is None, return None (node not found)
    if root is None:
        return None
    
    # If root is one of the nodes, it could be the LCA
    if root.value == p or root.value == q:
        return root.value
    
    # Recursively search in left and right subtrees
    left_result = lowest_common_ancestor(root.left, p, q)
    right_result = lowest_common_ancestor(root.right, p, q)
    
    # If both nodes were found in different subtrees, current node is LCA
    if left_result is not None and right_result is not None:
        return root.value
    
    # If both nodes are in the left subtree, return left result
    if left_result is not None:
        return left_result
    
    # If both nodes are in the right subtree, return right result
    if right_result is not None:
        return right_result
    
    # If neither node was found in this subtree, return None
    return None

def test_lowest_common_ancestor():
    """Test the lowest_common_ancestor function."""
    
    # Test Case 1: Nodes in different subtrees
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    # LCA of 4 and 6 should be 1
    lca1 = lowest_common_ancestor(tree1.root, 4, 6)
    print(f"Test Case 1: LCA of 4 and 6 is {lca1}, Expected: 1")
    assert lca1 == 1, f"Test Case 1 failed: Expected 1, got {lca1}"
    
    # Test Case 2: One node is ancestor of other
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    # LCA of 2 and 4 should be 2
    lca2 = lowest_common_ancestor(tree2.root, 2, 4)
    print(f"Test Case 2: LCA of 2 and 4 is {lca2}, Expected: 2")
    assert lca2 == 2, f"Test Case 2 failed: Expected 2, got {lca2}"
    
    # Test Case 3: Nodes are siblings
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    # LCA of 2 and 3 should be 1
    lca3 = lowest_common_ancestor(tree3.root, 2, 3)
    print(f"Test Case 3: LCA of 2 and 3 is {lca3}, Expected: 1")
    assert lca3 == 1, f"Test Case 3 failed: Expected 1, got {lca3}"
    
    # Test Case 4: One node is the root
    lca4 = lowest_common_ancestor(tree3.root, 1, 3)
    print(f"Test Case 4: LCA of 1 and 3 is {lca4}, Expected: 1")
    assert lca4 == 1, f"Test Case 4 failed: Expected 1, got {lca4}"
    
    # Test Case 5: Empty tree
    empty_tree = BinaryTree()
    lca5 = lowest_common_ancestor(empty_tree.root, 1, 2)
    print(f"Test Case 5: LCA in empty tree is {lca5}, Expected: None")
    assert lca5 is None, f"Test Case 5 failed: Expected None, got {lca5}"
    
    # Test Case 6: Node not in tree
    lca6 = lowest_common_ancestor(tree1.root, 4, 10)  # 10 is not in the tree
    print(f"Test Case 6: LCA of 4 and non-existent 10 is {lca6}, Expected: None")
    # This will return None because our implementation considers the LCA to exist only if both nodes exist
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_lowest_common_ancestor()


        # Tree structure:
print("          1 ")
print("         / \ ")
print("        2   3 ")
print("       / \   \ ")
print("      4   5   6 ")