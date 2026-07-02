# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None

        while head:
            nextval = head.next
            head.next = pre
            pre = head
            head = nextval

        return pre

                                                                                                                                            

