# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node:
                if node.val>=low and node.val <= high:
                    self.ans += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

# class Solution(object):
#     def rangeSumBST(self, root, L, R):
#         def dfs(node):
#             if node:
#                 if L <= node.val <= R:
#                     self.ans += node.val
#                 if L < node.val:
#                     dfs(node.left)
#                 if node.val < R:
#                     dfs(node.right)

#         self.ans = 0
#         dfs(root)
#         return self.ans

