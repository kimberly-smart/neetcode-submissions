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
        
        pre = None
        second = slow.next
        slow.next = None
        while second:
            secondnext = second.next
            second.next = pre
            pre = second
            second = secondnext
        
        first = head
        second = pre
        while second:
            firsttmp, secondtemp = first.next, second.next
            first.next = second
            second.next = firsttmp
            first = firsttmp
            second = secondtemp
        

        

    
    




            
        