class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        ans = R
        while L <= R:
            mid = (L+R)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)

            if hours <= h:
                ans = min(ans, mid)
                R = mid - 1
            else:
                L = mid + 1
        return ans