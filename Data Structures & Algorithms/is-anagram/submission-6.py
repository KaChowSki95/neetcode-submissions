class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = {}
        for i in s:
            if i in checkS:
                checkS[i] += 1
            else:
                checkS[i] = 1
        
        checkT = {}
        for i in t:
            if i in checkT:
                checkT[i] += 1
            else:
                checkT[i] = 1
        return checkS == checkT