# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        pre = None
        slow.next = None

        while second:
            nextnode = second.next
            second.next = pre
            pre = second
            second = nextnode
        
        first = head
        second = pre
        while second:
            fnext, snext = first.next, second.next
            first.next = second
            second.next = fnext
            second = snext
            first = fnext
        
        

        

    
    




            
        