class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        ans = 0
        for i in new:
            temp = 1
            while i + temp in new:
                temp += 1
            ans = max(ans, temp)
        return ans