class Solution:
    def countOfAtoms(self, formula: str) -> str:
        coef = 1
        atom = {}
        elem = ''
        stack = []
        count = ""
        num = 0
        i = 0
        for ch in formula[::-1] :
            if ch.isdigit() :
                num += int(ch) * (10 ** i)
                i += 1
            elif ch == ')' :
                num = num or 1
                stack.append(num)
                coef *= num
                i = num = 0
            elif ch == '(' :
                coef //= stack.pop()
            elif ch.isupper() :
                elem += ch
                elem = elem[::-1]
                if elem in atom :
                    atom[elem] += (num or 1) * coef
                else :
                    atom[elem] = (num or 1) * coef
                elem = ""
                i = num = 0
            elif ch.islower() :
                elem += ch
        res = ""
        for key in sorted(atom.keys()) :
            res += key
            if atom[key] > 1 :
                res += str(atom[key])
        return res