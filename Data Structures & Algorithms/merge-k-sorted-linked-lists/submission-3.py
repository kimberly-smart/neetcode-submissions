# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            curlist = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                curlist.append(self.combineval(l1, l2))
            lists = curlist
        
        return lists[0]
    
    def combineval(self, l1, l2):
        res = ListNode(0)
        reshead = res
        while l1 and l2:
            if l1.val < l2.val:
                reshead.next = l1
                l1 = l1.next
            else:
                reshead.next = l2
                l2 = l2.next
            reshead = reshead.next
        
        if l1:
            reshead.next = l1
        if l2:
            reshead.next = l2
        return res.next
            