class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None :
            return None 
        if root.val <= p.val :
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        if left is not None :
            return left 
        else :
            return root