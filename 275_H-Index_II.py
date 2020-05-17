class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations :
            return 0
        n = len(citations)
        l, r = 0, n-1
        while l+1 < r:
            mid = (l+r)//2
            if citations[mid] >= n-mid:
                r = mid
            else:
                l = mid
        if citations[l] >= n-l :
            return n-l
        elif citations[r] >= n-r :
            return n-r 
        return 0