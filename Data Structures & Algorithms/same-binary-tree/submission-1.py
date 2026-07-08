# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array1 = []
        array2 = []
        def check(node, array):
            if not node:
                array.append(0)
                return None
            array.append(node.val)
            check(node.left, array)
            check(node.right, array)
            return node
        check(p, array1)
        check(q, array2)
        return array1 == array2