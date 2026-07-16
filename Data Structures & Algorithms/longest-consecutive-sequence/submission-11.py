class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 0
        i = 0
        curr = nums[0]
        temp = 0
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                temp = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            temp += 1
            curr += 1
            ans = max(ans, temp)
        return ans