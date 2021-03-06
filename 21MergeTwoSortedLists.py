class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None and l2 is None: return None 
    
        curr = dummy = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
        
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
    
            curr.next = l1 or l2
        
        return dummy.next
