# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_val = l1.val + l2.val
        if curr_val >= 10:
            carry_on = curr_val // 10
            curr_val-=(10*carry_on)
        else:
            carry_on = 0
        
        head = ListNode(curr_val)
        curr = head
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            curr_val = carry_on + l1.val + l2.val
            if curr_val >= 10:
                carry_on = curr_val // 10
                curr_val-=(10*carry_on)
            else:
                carry_on = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_val = carry_on + l1.val
            if curr_val >= 10:
                carry_on = curr_val // 10
                curr_val-=(10*carry_on)
            else:
                carry_on = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next

        while l2:
            curr_val = carry_on + l2.val
            if curr_val >= 10:
                carry_on = curr_val // 10
                curr_val-=(10*carry_on)
            else:
                carry_on = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l2 = l2.next
        
        if carry_on > 0:
            curr.next = ListNode(carry_on)
        
        return head