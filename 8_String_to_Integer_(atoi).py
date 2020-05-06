class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0 :
            return 0
        ls = list(str.strip())
        if len(ls) == 0 :
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+'] :del ls[0]
        num, i = "", 0
        while i < len(ls) and ls[i].isdigit() :
            num += ls[i]
            i += 1 
        if not num :
            return 0
        res = int(num)
        return max(-(2<<30), min(sign * res, (2<<30 )- 1))