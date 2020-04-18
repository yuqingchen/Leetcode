class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre :
            return
        root = TreeNode(pre[0])
        if len(pre) == 1 :
            return root
        l = post.index(pre[1]) + 1 
        root.left = self.constructFromPrePost(pre[1 : l + 1], post[:l])
        root.right = self.constructFromPrePost(pre[l + 1 :], post[l : -1])
        return root