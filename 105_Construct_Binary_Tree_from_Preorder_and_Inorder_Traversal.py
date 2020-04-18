class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder :
            return
        root = TreeNode(preorder[0])
        rootpos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : rootpos + 1], inorder[: rootpos])
        root.right = self.buildTree(preorder[rootpos + 1 :], inorder[rootpos + 1 :])
        return root