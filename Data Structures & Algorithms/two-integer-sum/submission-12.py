class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            check = target - value
            if check in seen:
                return [seen[check], index]
            else:
                seen[value] = index