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
        ans = []
        if root is None:
            return ans
        ans.extend(self.inOrderTraversal(root.left))
        ans.append(root.val)
        ans.extend(self.inOrderTraversal(root.right))
        return ans

    def preOrderTraversal(self, root):
        # Steps for Pre Order Traversal
        # 1. Visit the root.
        # 2. Traverse the left subtree
        # 3. Traverse the right subtree
        ans = []
        if root is None:
            return ans
        ans.append(root.val)
        ans.extend(self.preOrderTraversal(root.left))
        ans.extend(self.preOrderTraversal(root.right))
        return ans

    def postOrderTraversal(self, root):
        # Steps for a Post Order Traversal
        # 1. Traverse the left subtree
        # 2. Traverse the right subtree
        # 3. Visit the root.
        ans = []
        if root is None:
            return ans
        ans.extend(self.postOrderTraversal(root.left))
        ans.extend(self.postOrderTraversal(root.right))
        ans.append(root.val)
        return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tree = Tree(root)
print tree.inOrderTraversal(root)
print ''
print tree.preOrderTraversal(root)
print ''
print tree.postOrderTraversal(root)
