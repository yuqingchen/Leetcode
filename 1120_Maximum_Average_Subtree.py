class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.node = None
        self.average = -sys.maxsize
        self.helper(root)
        return self.average 
    
    def helper(self, root) :
        if root is None :
            return 0, 0
        leftsum, leftsize = self.helper(root.left)
        rightsum, rightsize = self.helper(root.right)
        totalsum, size = leftsum + rightsum + root.val, leftsize + rightsize + 1
        if self.node is None or totalsum / size > self.average :
            self.node = root
            self.average = totalsum / size 
        return totalsum, size