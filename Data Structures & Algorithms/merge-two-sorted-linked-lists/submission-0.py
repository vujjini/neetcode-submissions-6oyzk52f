# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # have a pointer that represents the new list
        # have two pointers representing both the sorted lists
        # in each iteration (while both pointers are not None), have the next of the prev pointer point to minimum of both pointers
        # if both exist or point to whichever one that exists if only one of them exist. the pointer that was chosen to be the next,
        # update it to point to the next in its original list

        curr = None
        new_head = None
        if list1 and list2:
            if list1.val <= list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
        else:
            if list1:
                return list1
            if list2:
                return list2
            return None
        new_head = curr
        prev = curr
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    curr = list1
                    list1 = list1.next
                else:
                    curr = list2
                    list2 = list2.next
            else:
                if list1:
                    prev.next = list1
                    break
                else:
                    prev.next = list2
                    break
            prev.next = curr
            prev = curr

        return new_head