# This is a problem presented on Leetcode and this is my solution. The run time
# is O(n) and the space complexity is O(n).
#
#       4
#     /   \
#    2     7
#   / \   / \
#  1   3 6   9
#
#     to
#
#       4
#     /   \
#    7     2
#   / \   / \
#  9   6 3   1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        curRow = [root]
        nextRow = []
        temp = 0
        while curRow:
            for i in curRow:
                if i:
                    if i.right and i.left:
                        nextRow.append(i.right)
                        nextRow.append(i.left)
                        temp = i.left
                        i.left = i.right
                        i.right = temp
                    elif i.left and not i.right:
                        nextRow.append(None)
                        nextRow.append(i.left)
                        i.right = i.left
                        i.left = None
                    elif i.right and not i.left:
                        nextRow.append(None)
                        nextRow.append(i.right)
                        i.left = i.right
                        i.right = None
            curRow = nextRow
            nextRow = []
        return root

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)

            ret = Solution().invertTree(root)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
