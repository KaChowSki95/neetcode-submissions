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
        def search(node, check):
            if not node:
                check.append(0)
                return None
            check.append(node.val)
            search(node.left, check)
            search(node.right, check)
            return node
        search(p, check1)
        search(q, check2)
        return check1 == check2