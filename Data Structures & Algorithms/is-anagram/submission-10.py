class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checkS = {}
        checkT = {}
        for i in range(len(s)):
            if s[i] in checkS:
                checkS[s[i]] += 1
            else:
                checkS[s[i]] = 1
            
            if t[i] in checkT:
                checkT[t[i]] += 1
            else:
                checkT[t[i]] = 1
        return checkS == checkT