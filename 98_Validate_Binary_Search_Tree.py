class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.isBST = True
        self.lastval = None
        self.validate(root)
        print(self.isBST)
        return self.isBST
    
    def validate(self, root) :
        if not root :
            return
        self.validate(root.left)
        if self.lastval is not None and self.lastval >= root.val :
            self.isBST = False
            return 
        self.lastval = root.val
        self.validate(root.right)