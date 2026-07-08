class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in temp:
                return [temp[ans], i]
            else:
                temp[nums[i]] = i