class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 0 :
            return True
        for ch in s :
            if not ch.isalnum() :
                s = s.replace(ch, ' ')
        s = s.replace(' ', '')
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right :
            if s[left] != s[right] :
                return False
            else :
                left += 1
                right -= 1 
        return True