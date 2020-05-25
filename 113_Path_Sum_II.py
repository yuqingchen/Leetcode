class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, sum, [])
        return self.result
    
    def dfs(self, root, sum, path) :
        if not root :
            return
        if not root.left and not root.right and root.val == sum :
            self.result.append(path+[root.val])
        self.dfs(root.left, sum-root.val, path+[root.val])
        self.dfs(root.right, sum-root.val, path+[root.val])
        return