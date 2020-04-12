class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        la, lb = len(nums1), len(nums2)
        if (la + lb) % 2 == 1 :
            return self.find_kth(nums1, nums2, (la + lb) // 2 + 1)
        else :
            left = self.find_kth(nums1, nums2, (la + lb) // 2)
            right = self.find_kth(nums1, nums2, (la + lb) // 2 + 1)
            return (left + right) /2 
    
    def find_kth(self, nums1, nums2, k) :
        if len(nums1) == 0 :
            left, right = nums2[0], nums2[-1]
        elif len(nums2) == 0 :
            left, right = nums1[0], nums1[-1]
        else :
            left, right = min(nums1[0], nums2[0]), max(nums1[-1], nums2[-1])
        while left + 1 < right :
            mid = (left + right) // 2 
            count1 = self.count(nums1, mid)
            count2 = self.count(nums2, mid)
            if count1 + count2 < k :
                left = mid 
            else :
                right = mid 
        count1 = self.count(nums1, left)
        count2 = self.count(nums2, left)
        if count1 + count2 >= k :
            return left
        else :
            return right 
    
    def count(self, array, flag) :
        if len(array) == 0 :
            return 0 
        left, right = 0, len(array) - 1
        while left + 1 < right :
            mid = (left + right) // 2 
            if array[mid] < flag :
                left = mid 
            else :
                right = mid 
        if array[right] <= flag :
            return right + 1 
        if array[left] <= flag :
            return left + 1 
        return 0