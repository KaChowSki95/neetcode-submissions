class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in numSet:
            temp = 1
            while i + temp in numSet:
                temp += 1
            ans = max(ans, temp)
        return ans