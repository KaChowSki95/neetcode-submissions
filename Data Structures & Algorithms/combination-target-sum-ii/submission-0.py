class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def search(index, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if index >= len(candidates) or total > target:
                return
            curr.append(candidates[index])
            search(index + 1, curr, total + candidates[index])
            curr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            search(index + 1, curr, total)
        search(0, [], 0)
        return ans