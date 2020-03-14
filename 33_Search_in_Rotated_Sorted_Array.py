class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :
            return -1 
        start, end = 0 ,len(nums) - 1 
        while start + 1 < end :
            mid = (start + end) // 2
            if nums[mid] <= nums[end] :
                if nums[mid] <= target <= nums[end] :
                    start = mid 
                else :
                    end = mid 
            else :
                if nums[start] <= target <= nums[mid] :
                    end = mid 
                else :
                    start = mid 
            
        if nums[start] == target :
            return start
        if nums[end] == target :
            return end 
        return -1