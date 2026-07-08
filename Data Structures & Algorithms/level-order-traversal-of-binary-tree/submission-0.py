# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = collections.deque()
        que.append(root)
        while len(que) > 0:
            temp = []
            for i in range(len(que)):
                val = que.popleft()
                temp.append(val.val)
                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)
            ans.append(temp)
        return ans