class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for ele in s :
            if ele != ']' :
                stack.append(ele)
            else :
                alpha = ""
                while stack[-1] != '[' :
                    alpha += stack.pop()
                stack.pop()
                num = ""
                if stack and stack[-1].isalpha() :
                    num += '1'
                else :
                    while stack and stack[-1].isdigit() :
                        num += stack.pop()
                    num = num[::-1]
                temp = ""
                for i in range(int(num)) :
                    temp += alpha
                if len(stack) == 0 :
                    res = temp + res
                else :
                    alpha = ""
                    while stack and stack[-1] != '[' :
                        alpha += stack.pop()
                    temp += alpha
                    stack.append(temp)
        if len(stack) == 0 :
            return res[::-1]
        else:
            stack.reverse()
            alpha = "".join(stack)
            alpha += res
        return alpha[::-1]