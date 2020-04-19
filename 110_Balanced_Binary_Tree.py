class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced, height = self.isvalid(root)
        return balanced
    
    def isvalid(self, root) :
        if not root :
            return True, 0
        balanced, lefth = self.isvalid(root.left)
        if not balanced :
            return False, 0
        balanced, righth = self.isvalid(root.right)
        if not balanced:
            return False, 0
        return abs(lefth - righth) <= 1, max(lefth, righth) + 1
        