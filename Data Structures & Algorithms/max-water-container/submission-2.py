class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            if heights[L] < heights[R]:
                ans = max(ans, heights[L]*(R-L))
                L += 1
            else:
                ans = max(ans, heights[R]*(R-L))
                R -= 1
        return ans