class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        upper = root.val
        lower = root.val
        while root :
            if target > root.val :
                lower = root.val 
                root = root.right 
            elif target < root.val :
                upper = root.val
                root = root.left 
            else :
                return root.val 
        if abs(target - lower) < abs(upper - target) :
            return lower
        else :
            return upper