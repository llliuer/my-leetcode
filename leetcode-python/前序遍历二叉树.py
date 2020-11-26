
#144.二叉树的前序遍历
#https://leetcode-cn.com/problems/binary-tree-preorder-traversal/submissions/
#

#递归，对一个节点，先输出根节点，再递归输出左节点右节点
#结束返回条件是遍历到空节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if root == None:
                return root
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)
        return res

#官方题解：
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         def preorder(root: TreeNode):
#             if not root:
#                 return
#             res.append(root.val)
#             preorder(root.left)
#             preorder(root.right)

#         res = list()
#         preorder(root)
#         return res