class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = L + (R-L)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[L] > target and nums[mid] > target:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                if nums[R] < target and nums[mid] > target:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1