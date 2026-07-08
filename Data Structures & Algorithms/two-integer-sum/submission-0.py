class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for key, value in enumerate(nums):
            check = target - value
            if check in dic:
                return [dic[check], key]
            else:
                dic[value] = key