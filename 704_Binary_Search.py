class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end :
            mid = (start + end) // 2
            if nums[mid] < target :
                start = mid
            elif nums[mid] == target :
                start = mid
            else :
                end = mid
        if nums[start] == target :
            return start
        if nums[end] == target :
            return end
        return -1