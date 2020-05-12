class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = self.twopointer(0, len(s) - 1, s)
        if left >= right :
            return True
        return self.valid(left + 1, right, s) or self.valid(left, right - 1, s)
    
    def valid(self, left, right, s) :
        l, r = self.twopointer(left, right, s)
        if l >= r :
            return True
        else:
            return False
    
    def twopointer(self, left, right, s) :
        while left < right :
            if s[left] == s[right] :
                left += 1
                right -= 1
            else :
                return left, right
        return left, right