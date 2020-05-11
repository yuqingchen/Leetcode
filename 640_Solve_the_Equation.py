class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        k1, b1 = self.helper(left)
        k2, b2 = self.helper(right)
        print(k1)
        print(b1)
        print(k2)
        print(b2)
        if k1 != k2 and b1 != b2 :
            return 'x=' + str((b2 - b1) // (k1 - k2))
        elif k1 == k2 and b1 == b2 :
            return "Infinite solutions"
        elif b1 == b2 :
            return "x=0"
        else :
            return "No solution"
        
    def helper(self, s) :
        sign, n = 1, len(s)
        i, coef, const = 0, 0, 0
        while i < n :
            if s[i] == '+' :
                sign = 1
            elif s[i] == '-' :
                sign = -1
            elif s[i].isdigit() :
                j = i
                while j < n and s[j].isdigit() :
                    j += 1
                tmp = int(s[i : j])
                if j < n and s[j] == 'x' :
                    coef += tmp * sign
                    j += 1
                else :
                    const += tmp * sign
                i = j - 1
            else :
                coef += 1 * sign
            i += 1
        return coef, const