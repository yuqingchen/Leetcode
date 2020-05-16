class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = bigger = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i] :
            i -= 1
        if i == 0 :
            nums.reverse()
            return
        pivot = i-1
        while nums[bigger] <= nums[pivot] :
            bigger -= 1 
        nums[pivot], nums[bigger] = nums[bigger], nums[pivot]
        l, r = pivot+1, len(nums)-1
        while l < r :
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1