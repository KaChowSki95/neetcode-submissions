class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)
        for i in numSet:
            temp = 1
            while i + temp in numSet:
                temp += 1
            ans = max(ans, temp)
        return ans