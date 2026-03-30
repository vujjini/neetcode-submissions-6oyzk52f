import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = []
        visited = set()
        heapq.heappush(minHeap, (0, 0))
        res = 0
        n = len(points)

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            for i in range(n):
                if i in visited:
                    continue
                manhattanDist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                heapq.heappush(minHeap, (manhattanDist, i))
        
        return res