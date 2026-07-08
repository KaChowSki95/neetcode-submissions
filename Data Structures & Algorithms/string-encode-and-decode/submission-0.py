class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i))+"#"+i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        while index < len(s):
            temp = index
            while s[temp] != "#":
                temp += 1
            length = int(s[index:temp])
            ans.append(str(s[temp + 1: temp + 1 + length]))
            index = temp + 1 + length
        return ans