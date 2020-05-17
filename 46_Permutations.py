class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, path) :
        if not nums :
            self.res.append(path[:])
            return
        for i in range(len(nums)) :
            path.append(nums[i])
            self.dfs(nums[:i]+nums[i+1:], path)
            path.pop()