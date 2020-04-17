class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root :
            return []
        res, stack, cur = [], [], root
        while cur :
            stack.append(cur)
            if cur.left :
                cur = cur.left 
            else :
                cur = cur.right 
        
        while stack :
            cur = stack.pop()
            res.append(cur.val)
            if stack and stack[-1].left == cur :
                cur = stack[-1].right 
                while cur :
                    stack.append(cur)
                    if cur.left :
                        cur = cur.left 
                    else :
                        cur = cur.right 
        return res