class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        check = {}
        for i in nums:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        for number, count in check.items():
            buckets[count].append(number)
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans