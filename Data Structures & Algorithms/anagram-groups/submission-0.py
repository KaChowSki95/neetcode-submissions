class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        check = {}
        for i in strs:
            if ''.join(sorted(i)) in check:
                check[''.join(sorted(i))].append(i)
            else:
                check[''.join(sorted(i))] = [i]
        for i in check:
            ans.append(check[i])
        return ans