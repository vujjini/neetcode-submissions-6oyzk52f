class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for coords in points:
            minHeap.append((coords[0]**2 + coords[1]**2, coords))
        
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res