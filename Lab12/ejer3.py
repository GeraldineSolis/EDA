class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Rotar
        y.left = z
        z.right = T2

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Rotar
        y.right = z
        z.left = T3

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        # Paso normal de BST
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Actualizar altura
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Obtener balance
        balance = self.get_balance(root)

        # Caso LL
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Caso RR
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Caso LR
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Caso RL
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        # Paso 1: BST delete normal
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Nodo con uno o cero hijos
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Nodo con dos hijos: obtener sucesor inorder
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Si el árbol solo tenía un nodo
        if root is None:
            return root

        # Actualizar altura
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Revisar balance
        balance = self.get_balance(root)

        # Caso LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Caso LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Caso RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Caso RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# 🧪 Pruebas para delete

def test_avl_delete():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)

    root = avl.delete(root, 35)
    print("🧪 Test 1 (Delete leaf 35):", end=" ")
    avl.inorder(root)
    print()

    root = avl.delete(root, 25)
    print("🧪 Test 2 (Delete one child 25):", end=" ")
    avl.inorder(root)
    print()

    root = avl.delete(root, 20)
    print("🧪 Test 3 (Delete two children 20):", end=" ")
    avl.inorder(root)
    print()

    print("🧪 Test 4 & 5 (Balanced tree after deletes):", end=" ")
    avl.inorder(root)
    print()

test_avl_delete()
