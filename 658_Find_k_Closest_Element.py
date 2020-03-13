class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0 
        end = len(arr) - 1 
        if arr[0] > x :
            right = 0
        while start + 1 < end :
            mid = (start + end) // 2 
            if arr[mid] < x :
                start = mid 
            else :
                end = mid 
        if arr[start] >= x :
            right = start 
        if arr[end] >= x :
            right = end 
        left = right - 1 
        res = []
        for _ in range(k) :
            if self.isLeftCloser(arr, left, right, x) :
                res.append(arr[left])
                left -= 1 
            else :
                res.append(arr[right])
                right += 1 
        res.sort()
        return res
    
    def isLeftCloser(self, arr, left, right, x) :
        if left < 0 :
            return False
        if right >= len(arr) :
            return True 
        return x - arr[left] <= arr[right] - x