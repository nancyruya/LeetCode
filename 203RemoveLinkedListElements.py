class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        previous, current = dummy, dummy.next
        
        while current:
            if current.val == val:
                previous.next = current.next         
            else:
                previous = current
            current = current.next
        return dummy.next
