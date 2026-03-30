# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode(0)
        prev = dummy
        
        while minHeap:
            val, i, curr = heapq.heappop(minHeap)
            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, i, curr.next))
            prev.next = curr
            prev = curr
        
        return dummy.next
