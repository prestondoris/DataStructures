class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = root

    def inOrderTraversal(self, root):
        # Steps for In Order Traversal
        # 1. Traverse the left subtree
        # 2. Visit the root.
        # 3. Traverse the right subtree
        if root:
            self.inOrderTraversal(root.left)
            print root.val
            self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root):
        # Steps for Pre Order Traversal
        # 1. Visit the root.
        # 2. Traverse the left subtree
        # 3. Traverse the right subtree
        if root:
            print root.val
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        # Steps for a Post Order Traversal
        # 1. Traverse the left subtree
        # 2. Traverse the right subtree
        # 3. Visit the root.
        if root:
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
            print root.val

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tree = Tree(root)
tree.inOrderTraversal(root)
print ''
tree.preOrderTraversal(root)
print ''
tree.postOrderTraversal(root)
