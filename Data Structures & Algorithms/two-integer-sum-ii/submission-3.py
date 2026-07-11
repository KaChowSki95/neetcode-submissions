class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            check = numbers[L] + numbers[R]
            if check < target:
                L += 1
            elif check > target:
                R -= 1
            else:
                return [L+1, R+1]