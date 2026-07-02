# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        second = slow.next
        slow.next = None

        while second:
            nexsec = second.next
            second.next = pre
            pre = second
            second = nexsec
        
        first = head
        second = pre
        while second:
            fnext, snext = first.next, second.next
            first.next = second
            second.next = fnext
            second = snext
            first = fnext

        
        

        

    
    




            
        