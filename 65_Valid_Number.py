class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num = s.split("e")
        print(num)
        if len(num) > 2 :
            return False
        if len(num) == 2 :
            left = self.checkleft(num[0])
            right = self.checkright(num[1])
        elif len(num) == 1 :
            left = self.checkleft(num[0])
            right = True
        if left and right :
            return True
        else :
            return False
      
    def checkleft(self, s) :
        if len(s) == 0 :
            return False
        i = 0
        if s[0] in ['-', '+']:
            if len(s) < 2 :
                return False
            else:
                i += 1
        n = len(s)
        sign = False
        while i < n :
            if s[i] == '.' :
                if i + 1 < n and s[i + 1].isdigit() and not sign:
                    i += 1
                    sign = True
                elif 0 <= i - 1 and s[i - 1].isdigit() and not sign:
                    i += 1
                    sign = True
                else :
                    return False
            elif not s[i].isdigit() :
                return False
            elif s[i] in ['+', '-'] :
                return False
            else :
                i += 1
        return True
        
        
    def checkright(self, s) :
        if len(s) == 0 :
            return False
        i = 0
        if s[0] in ['-', '+'] :
            if len(s) < 2 :
                return False
            else:
                i += 1
        n = len(s)
        while i < n :
            if s[i] == '.' :
                return False
            elif not s[i].isdigit() :
                return False
            elif s[i] in ['+', '-'] :
                return False
            i += 1
        return True