# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            ans = ListNode(l2.val)
            ans.next = self.mergeTwoLists(l1, l2.next)
        else:
            ans = ListNode(l1.val)
            ans.next = self.mergeTwoLists(l1.next, l2)
        return ans
        

        
        
"""
[1,2,4]

[1,3,4]


1. 


1. 1=1



3,4




"""