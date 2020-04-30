class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        results = []
        if root is None :
            return results
        prestack, nextstack = self.getstack(root, target)
        for i in range(k) :
            if len(prestack) == 0 and len(nextstack) == 0 :
                return results
            predis = sys.maxsize if len(prestack) == 0 else abs(prestack[-1].val - target)
            nextdis = sys.maxsize if len(nextstack) == 0 else abs(nextstack[-1].val - target)
            if predis < nextdis :
                results.append(self.getpre(prestack))
            else :
                results.append(self.getnext(nextstack))
        return results
    
    def getstack(self, root, target) :
        prestack, nextstack = [], []
        while root :
            if root.val < target :
                prestack.append(root)
                root = root.right
            else :
                nextstack.append(root)
                root = root.left 
        return prestack, nextstack
    
    def getpre(self, prestack) :
        cur = prestack.pop()
        value = cur.val
        node = cur.left
        while node :
            prestack.append(node)
            node = node.right 
        return value
    
    def getnext(self, nextstack) :
        cur = nextstack.pop()
        value = cur.val
        node = cur.right 
        while node :
            nextstack.append(node)
            node = node.left 
        return value