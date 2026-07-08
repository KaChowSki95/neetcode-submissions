class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsets(index, curr):
            if index >= len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[index])
            subsets(index + 1, curr)
            curr.pop()
            subsets(index + 1, curr)
        subsets(0, [])
        return ans