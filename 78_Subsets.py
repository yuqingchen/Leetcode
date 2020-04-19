class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.search(nums, [], 0)
        return self.result 
    
    def search(self, nums, s, index) :
        if len(nums) == index:
            self.result.append(list(s))
            return
        s.append(nums[index])
        self.search(nums, s, index + 1)
        s.pop()
        self.search(nums, s, index + 1)