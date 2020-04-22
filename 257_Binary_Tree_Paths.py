class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None :
            return [str(root.val)]
        leftpath = self.binaryTreePaths(root.left)
        rightpath = self.binaryTreePaths(root.right)
        paths = []
        for path in leftpath + rightpath :
            paths.append(str(root.val) + '->' +path)
        return paths