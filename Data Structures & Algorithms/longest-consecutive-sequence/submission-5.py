class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for i in set(nums):
            temp = 1
            while i + temp in set(nums):
                temp += 1
            ans = max(ans, temp)
        return ans