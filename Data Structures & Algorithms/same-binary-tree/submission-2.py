# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check1 = []
        check2 = []
        def checkTree(node, check):
            if not node:
                check.append(None)
                return
            check.append(node.val)
            checkTree(node.left, check)
            checkTree(node.right, check)
        checkTree(p, check1)
        checkTree(q, check2)
        return check1 == check2