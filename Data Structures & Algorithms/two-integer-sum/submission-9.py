class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, value in enumerate(nums):
            comp = target - value
            if comp in check:
                return [check[comp], index]
            else:
                check[value] = index