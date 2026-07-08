class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        ans = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                ans = min(ans, nums[L])
                return ans
            mid = (L+R)//2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
        return ans
                