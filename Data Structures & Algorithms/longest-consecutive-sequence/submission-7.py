class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        ans = 0
        for i in newSet:
            temp = 1
            while i + temp in newSet:
                temp += 1
            ans = max(ans, temp)
        return ans