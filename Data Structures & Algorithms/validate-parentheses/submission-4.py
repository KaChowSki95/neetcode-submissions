class Solution:
    def isValid(self, s: str) -> bool:
        check = {"}":"{", "]":"[", ")":"("}
        ans = []
        for i in s:
            if i in check:
                if ans and ans[-1] == check[i]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(i)
        return len(ans) == 0