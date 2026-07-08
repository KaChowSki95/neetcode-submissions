class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        check = {}
        L = 0
        for R in range(len(s)):
            if s[R] in check:
                check[s[R]] += 1
            else:
                check[s[R]] = 1
            
            if (R-L+1) - max(check.values()) > k:
                check[s[L]] -= 1
                L += 1
            ans = max(ans, R-L+1)
        return ans