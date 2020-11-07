# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        res = []

        if root == None:
            return 0

        if root.left == None or root.right == None:
            if root.left:
                return root.val * 10 + root.left.val
            if root.right:
                return root.val * 10 + root.right.val

        frontnum = ''

        def FindNum(root, frontnum):

            if root.left:
                FindNum(root.left, frontnum + str(root.val))
            if root.right:
                FindNum(root.right, frontnum + str(root.val))

            if (root.left == None and root.right == None):
                res.append(int(frontnum + str(root.val)))
                return

        FindNum(root, frontnum)

        SUM = 0
        for i in res:
            SUM = SUM + i
        return SUM


inputstr = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]

New_Tree = t = TreeNode(inputstr[0])
for i in range(1, len(inputstr)):
    New_TreeNode = TreeNode(inputstr[i])
    t.left = New_TreeNode
    t = t.left
S = Solution()
print(S.sumNumbers(New_Tree))
