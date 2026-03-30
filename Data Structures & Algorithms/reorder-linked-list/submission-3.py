# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            if not head or not head.next:
                return head
            prev = head
            curr = head.next

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            head.next = None
            
            return prev
        
        middle = head
        fast = head

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        
        # reverse
        
        end = reverse(middle.next)
        middle.next = None

        p1 = head
        p2 = end

        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next






        
        


        
        