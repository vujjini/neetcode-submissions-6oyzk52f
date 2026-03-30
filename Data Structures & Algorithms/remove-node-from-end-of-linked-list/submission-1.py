# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        end = head
        remove = head
        prev = None

        for _ in range(n):
            end = end.next
        
        while end:
            end = end.next
            prev = remove
            remove = remove.next
        
        if not prev:
            return remove.next
        
        if not remove.next:
            prev.next = None
        
        prev.next = remove.next

        return head