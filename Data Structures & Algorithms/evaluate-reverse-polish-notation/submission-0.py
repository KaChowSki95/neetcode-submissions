class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for i in tokens:
            if i == '+':
                temp = ans.pop()
                ans[-1] = ans[-1] + temp
            elif i == '-':
                temp = ans.pop()
                ans[-1] = ans[-1] - temp
            elif i == '*':
                temp = ans.pop()
                ans[-1] = ans[-1] * temp
            elif i == '/':
                temp = ans.pop()
                ans[-1] = int(ans[-1]/temp)
            else:
                ans.append(int(i))
        return sum(ans)