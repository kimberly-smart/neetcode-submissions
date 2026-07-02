# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists)<1: 
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if len(lists) > i+1 else None
                mergedLists.append(self.mergetwoLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]
        
    def mergetwoLists(self, list1, list2):
        dummy = ListNode(0)
        res = dummy

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        
        res.next = list1 or list2

        return dummy.next