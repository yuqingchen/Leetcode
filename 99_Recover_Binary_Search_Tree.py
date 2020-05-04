class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node = []
        self.value = []
        self.inorder(root)
        self.value.sort()
        for i in range(len(self.node)) :
            self.node[i].val = self.value[i]
        return root
        
    def inorder(self, root) :
        if root is None :
            return
        self.inorder(root.left)
        self.node.append(root)
        self.value.append(root.val)
        self.inorder(root.right)