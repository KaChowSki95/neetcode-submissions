class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        temp = {}
        for i in strs:
            if "".join(sorted(i)) in temp:
                temp["".join(sorted(i))].append(i)
            else:
                temp["".join(sorted(i))] = [i]
        for i in temp:
            ans.append(temp[i])
        return ans