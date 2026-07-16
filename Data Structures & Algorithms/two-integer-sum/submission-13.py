class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, value in enumerate(nums):
            compl = target - value
            if compl in check:
                return [check[compl], index]
            check[value] = index