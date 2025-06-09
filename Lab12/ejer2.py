class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def rotate_left(self, z):
        """🔄 Perform left rotation on node z"""
        y = z.right  # el hijito derecho sube
        T2 = y.left  # el subarbol izquierdo del hijito derecho

        # Hacemos la rotación
        y.left = z
        z.right = T2

        # Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # nuevo papá

    def rotate_right(self, z):
        """🔁 Perform right rotation on node z"""
        y = z.left  # el hijito izquierdo sube
        T3 = y.right  # el subarbol derecho del hijito izquierdo

        # Hacemos la rotación
        y.right = z
        z.left = T3

        # Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # nuevo papá

# 🧪 Test rotations
def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z.height = 2
    z.right.height = 2
    z = tree.rotate_left(z)
    print("🧪 Test 1 (Left Rotation OK?):", z.key == 20)  # ✅

    # Test 2: Right Rotation
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z.height = 2
    z.left.height = 2
    z = tree.rotate_right(z)
    print("🧪 Test 2 (Right Rotation OK?):", z.key == 20)  # ✅

    # Test 3–5: Heights and child structure
    print("🧪 Test 3 (Heights):")
    print(f"Root: {z.key}, Height: {z.height}")
    print(f"Left: {z.left.key}, Height: {z.left.height}")
    print(f"Right: {z.right.key}, Height: {z.right.height}")

# 🚀 Run tests
test_rotations()
