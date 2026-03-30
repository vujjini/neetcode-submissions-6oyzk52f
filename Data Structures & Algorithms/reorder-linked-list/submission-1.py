# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        middle = fast = head
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        
        prev = middle.next
        middle.next = None
        if not prev:
            return
        curr = prev.next
        prev.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        second_list = prev

        while head and second_list:
            first_tmp = head.next
            second_tmp = second_list.next
            head.next = second_list
            second_list.next = first_tmp

            head = first_tmp
            second_list = second_tmp

        