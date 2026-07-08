class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            L = index + 1
            R = len(nums) - 1
            while L < R:
                check = number + nums[L] + nums[R]
                if check > 0:
                    R -= 1
                elif check < 0:
                    L += 1
                else:
                    ans.append([number, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return ans