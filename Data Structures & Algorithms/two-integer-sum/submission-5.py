class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in temp:
                return [temp[check], i]
            else:
                temp[nums[i]] = i
