class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res
    
    def traverse(self, root, res) :
        if not root:
            return
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        