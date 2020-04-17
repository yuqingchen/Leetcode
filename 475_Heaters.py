class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses :
            ans = max(ans, self.findheater(house, heaters)) 
        return ans
    
    def findheater(self, house, heaters) :
        start, end = 0, len(heaters) - 1 
        while start + 1 < end :
            mid = (start + end) // 2 
            if heaters[mid] == house :
                return 0
            if heaters[mid] < house :
                start = mid 
            else :
                end = mid 
        return min(abs(house - heaters[start]), abs(heaters[end] - house))
        