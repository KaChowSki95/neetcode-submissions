class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        L = 0
        R = 1
        while R < len(prices):
            if prices[R] > prices[L]:
                ans = max(ans, prices[R]-prices[L])
            else:
                L = R
            R += 1
        return ans