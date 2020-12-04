# 654. 最大二叉树
# https://leetcode-cn.com/problems/maximum-binary-tree/
#





# My Solution:
# 取最大值为新节点，对左边右边分别进行递归构造，终止条件为长度为0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(nums):  # i, j 为下标索引
            if len(nums) == 0:
                return None
            maxnum = max(nums)
            maxindex = nums.index(maxnum)

            newNode = TreeNode(maxnum)
            newNode.left = dfs(nums[:maxindex])
            newNode.right = dfs(nums[maxindex + 1:])

            return newNode

        return dfs(nums)
