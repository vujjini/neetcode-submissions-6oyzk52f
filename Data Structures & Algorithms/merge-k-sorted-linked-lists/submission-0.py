# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # index each list into a map with value as currNode in that list. Remove the key val if val goes to None
        # each iteration loop through all nodes (vals) in the map to get the next node in the res list
            # update the val to next (remove if next is None)
        
        nodes = {}
        for i in range(len(lists)):
            if lists[i]:
                nodes[i] = lists[i]
        
        dummy = ListNode(0)
        prev = dummy
        
        while nodes:
            currMin = float('inf')
            for i in nodes:
                if nodes[i].val <= currMin:
                    currMin = nodes[i].val
                    nextIdx = i
            currNode = ListNode(nodes[nextIdx].val)
            prev.next = currNode
            nodes[nextIdx] = nodes[nextIdx].next
            if not nodes[nextIdx]:
                nodes.pop(nextIdx)
            prev = currNode
        
        return dummy.next
        
