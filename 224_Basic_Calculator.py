class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, num, sign = 0, 0, 1
        for ch in s:
            if ch.isdigit() :
                num = 10*num + int(ch)
            elif ch in ['+', '-'] :
                res += num*sign
                sign = [1, -1][ch == '-']
                num = 0
            elif ch == '(' :
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif ch == ')' :
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
            