class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res
    
    def traverse(self, root, res) :
        if not root :
            return
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)