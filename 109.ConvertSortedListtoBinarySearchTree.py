class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        
        #1, 2, 3, 4, 5
        
        def findMid(head):
            slow = fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
                
        
        mid = findMid(head)
        root = TreeNode(mid.val)
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
