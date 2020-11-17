# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# preorder = [15,9,20, 3,7]
# inorder = [ 9,3,15,20,7]
#     idx = [ 0,1, 2, 3,4]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder or not inorder:  # 递归终止条件
#             return
#         root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
#         idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
#         # 下面递归对root的左右子树求解即可
#         root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
#         root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
#         return root


# if len(preorder) == 0:
#     return None
# if len(preorder) == 1:
#     return TreeNode(preorder.pop(0))

# def buildTreedfs(inorder, begin, end):
#     if end - begin == 0:
#         return None
#     elif end-begin == 1:
#         return TreeNode(preorder.pop(0))
#     i = preorder.pop(0)
#     newNode = TreeNode(i)
#     rootindex = inorder.index(i)
#     newNode.left = buildTreedfs(inorder, begin, rootindex)
#     newNode.right = buildTreedfs(inorder, rootindex+1, end)
#     return newNode

# begin = 0
# end = len(preorder)-1
# i = preorder.pop(0)
# res = TreeNode(i)
# rootindex = inorder.index(i)
# res.left = buildTreedfs(inorder, begin, rootindex)
# res.right = buildTreedfs(inorder, rootindex+1, end+1)
# return res
