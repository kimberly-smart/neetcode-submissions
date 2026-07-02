# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists)>1:
            mergelist = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergelist.append(self.mergeList(l1, l2))
            lists = mergelist

        return lists[0]


    
            

      
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        dummyhead = dummy

        while l1 and l2:
            if l1.val > l2.val:
                dummyhead.next = l2
                l2 = l2.next
            else:
                dummyhead.next = l1
                l1 = l1.next
            dummyhead = dummyhead.next

        if l1:
            dummyhead.next = l1
        if l2:
            dummyhead.next = l2
        
        return dummy.next
       
