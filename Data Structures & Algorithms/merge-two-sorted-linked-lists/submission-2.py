# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummyhead = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummyhead.next = list1
                list1 = list1.next
            else:
                dummyhead.next = list2
                list2 = list2.next
            dummyhead = dummyhead.next
        
        if list1:
            dummyhead.next = list1
        if list2:
            dummyhead.next = list2
        return dummy.next
