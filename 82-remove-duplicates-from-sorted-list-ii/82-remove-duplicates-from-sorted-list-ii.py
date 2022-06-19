# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy 
        cur = head
        
        while cur and cur.next:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            
            if prev.next == cur:
                prev = prev.next
            
            else:
                prev.next = cur.next
            cur = cur.next
            
        return dummy.next