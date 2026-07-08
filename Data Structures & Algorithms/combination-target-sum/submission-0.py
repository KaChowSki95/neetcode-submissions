class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def search(index, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if index >= len(nums) or total > target:
                return
            curr.append(nums[index])
            search(index, curr, total + nums[index])
            curr.pop()
            search(index + 1, curr, total)
        search(0, [], 0)
        return ans