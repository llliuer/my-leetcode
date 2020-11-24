# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def setdeepdfs(root, deep):
            deep = deep + 1
            if root == None:
                return root
            else:
                root.val = [root.val, deep]
                setdeepdfs(root.left, deep)
                setdeepdfs(root.right, deep)

        def orderdfs(r):
            if r == None:
                return r
            else:
                if r.val[1] in hs:
                    hs[r.val[1]].append(r.val[0])
                else:
                    hs[r.val[1]] = [r.val[0]]
                orderdfs(r.left)
                orderdfs(r.right)

        if root == None:
            return []
        root.val = [root.val, 0]
        setdeepdfs(root.left, 0)
        setdeepdfs(root.right, 0)

        hs = {}
        orderdfs(root)
        res = []
        for i in range(len(hs)):
            res.append(hs[i])

        return res
