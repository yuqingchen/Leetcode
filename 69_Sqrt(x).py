class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start + 1 < end :
            mid = (start+end)//2
            if mid*mid <= x :
                start = mid
            else :
                end = mid
        if end*end <= x :
            return end
        return start