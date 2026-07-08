class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def subsets(index, curr):
            if index >= len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[index])
            subsets(index + 1, curr)
            curr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            subsets(index + 1, curr)
        subsets(0, [])
        return ans