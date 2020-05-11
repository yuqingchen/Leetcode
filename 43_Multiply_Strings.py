class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0' :
            return '0'
        multi = [0 for i in range(len(num1) + len(num2))]
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        for i in range(len(num1)) :
            for j in range(len(num2)) :
                multi[i + j] += int(num1[i]) * int(num2[j])
        res = ''
        for i in range(len(multi)) :
            res += str(multi[i] % 10)
            if i + 1 < len(multi) :
                multi[i + 1] += multi[i] // 10
            else :
                break
        i = len(multi) - 1
        while multi[i] == 0 :
            i -= 1
        return res[:i + 1][::-1]