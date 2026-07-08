class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = {}
        for i in s:
            if i in check1:
                check1[i] += 1
            else:
                check1[i] = 1
        check2 = {}
        for i in t:
            if i in check2:
                check2[i] += 1
            else:
                check2[i] = 1
        return check1 == check2