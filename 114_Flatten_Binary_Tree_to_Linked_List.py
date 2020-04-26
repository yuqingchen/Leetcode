class Solution:
    node = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None :
            return
        if self.node is not None :
            self.node.left = None
            self.node.right = root
        self.node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)