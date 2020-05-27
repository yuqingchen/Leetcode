class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums :
            return 
        n = len(nums) - k
        res = self.quickselect(nums, n, 0, len(nums) - 1)
        return res 
    
    def quickselect(self, nums, n, start, end) :
        if start >= end :
            return nums[end]
        mid = (start + end) // 2 
        pivot = nums[mid]
        l, r = start, end 
        while l  <= r :
            while l <= r and nums[l] < pivot :
                l += 1 
            while l <= r and nums[r] > pivot :
                r -= 1 
            if l <= r :
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
        if r >= n :
            return self.quickselect(nums, n, start, r)
        if l <= n :
            return self.quickselect(nums, n, l, end)
        else :
            return nums[n]