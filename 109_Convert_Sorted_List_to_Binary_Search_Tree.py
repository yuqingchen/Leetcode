class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        length = self.getlength(head)
        root, next = self.convert(head, length)
        return root
    
    def getlength(self, head) :
        length = 0
        while head :
            length += 1
            head = head.next
        return length
    
    def convert(self, head, length) :
        if length == 0 :
            return None, head
        left, middle = self.convert(head, length // 2)
        right, next = self.convert(middle.next, length - length // 2 - 1)
        root = TreeNode(middle.val)
        root.left = left
        root.right = right 
        return root, next