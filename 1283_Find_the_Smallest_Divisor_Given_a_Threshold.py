import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        while start + 1 < end :
            mid = (start + end) // 2
            if self.divisionsum(nums, mid) > threshold :
                start = mid 
            else :
                end = mid
        if self.divisionsum(nums, start) <= threshold :
            return start
        else :
            return end
    
    def divisionsum(self, nums, divisor) :
        res = 0
        for num in nums :
            res += math.ceil((num / divisor))
        return res