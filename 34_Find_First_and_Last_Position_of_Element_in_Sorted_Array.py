class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.first(nums, target), self.last(nums, target)
        return [left, right]
    
    def last(self, nums, target) :
        if not nums :
            return -1
        left, right = 0, len(nums) -1
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] <= target :
                left = mid 
            else :
                right = mid 
        if nums[right] == target :
            return right
        if nums[left] == target :
            return left
        return -1
    
    def first(self, nums, target) :
        if not nums :
            return -1
        left, right = 0, len(nums) -1
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid 
            else :
                right = mid 
        if nums[left] == target :
            return left
        if nums[right] == target :
            return right
        return -1