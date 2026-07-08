class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            L = index + 1
            R = len(nums) - 1
            while L < R:
                check = num + nums[L] + nums[R]
                if check > 0:
                    R -= 1
                elif check < 0:
                    L += 1
                else:
                    ans.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return ans