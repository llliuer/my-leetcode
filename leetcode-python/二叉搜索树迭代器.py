
# 173. 二叉搜索树迭代器
# https://leetcode-cn.com/problems/binary-search-tree-iterator/

#

# 受控递归，使用迭代的方式控制递归前进。
# 将root及root.left依次入栈，栈顶即为最小元素，出栈时，如果栈顶为叶子节点，那么直接出栈，
# 如果栈顶元素还有右孩子，那么将有孩子的左孩子入栈
# 空间复杂度为O(h)H为树的高度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.helper(root)

    def next(self) -> int:
        a = self.stack.pop()
        if a.right != None:
            self.helper(a.right)

        return a.val

    def hasNext(self) -> bool:
        if len(self.stack) != 0:
            return True
        else:
            return False

    def helper(self, root):
        if root:
            self.stack.append(root)
            self.helper(root.left)


# 递归
# 初始化时用中序遍历将二叉树存入数组，数组即为升序。
# 空间复杂度为O(n)

# class BSTIterator:

#     def __init__(self, root: TreeNode):

#         self.l = []
#         self.index = 0

#         self._inorder(root)
#         self.lens = len(self.l)

#     def _inorder(self,root):
#         if root == None:
#             return
#         self._inorder(root.left)
#         self.l.append(root.val)
#         self._inorder(root.right)

#     def next(self) -> int:
#         self.index += 1
#         return self.l[self.index-1]

#     def hasNext(self) -> bool:
#         #print(self.l, self.index)
#         if self.index == self.lens:
#             return False
#         else:
#             return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()