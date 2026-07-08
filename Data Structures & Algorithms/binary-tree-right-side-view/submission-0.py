# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = collections.deque()
        que.append(root)
        ans = []
        while len(que) > 0:
            right = None
            for i in range(len(que)):
                temp = que.popleft()
                right = temp.val
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            ans.append(right)
        return ans