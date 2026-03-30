# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        curr_sum = l1.val + l2.val
        curr_digit = curr_sum
        if curr_sum >= 10:
            carry = 1
            curr_digit = curr_sum - 10
        res = ListNode(curr_digit)
        prev = res
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            curr_sum = carry
            carry = 0
            if l1:
                curr_sum += l1.val
            if l2:
                curr_sum +=l2.val
            curr_digit = curr_sum
            if curr_sum >= 10:
                carry = 1
                curr_digit = curr_sum - 10
            prev.next = ListNode(curr_digit)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            prev.next = ListNode(carry, None)

        return res