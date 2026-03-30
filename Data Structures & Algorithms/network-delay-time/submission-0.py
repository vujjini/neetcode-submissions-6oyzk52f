class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        
        for edge in times:
            adj[edge[0]].append((edge[2], edge[1]))
        print(adj)
        
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        res = 0
        visited = set()

        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            res = max(res, currTime)
            visited.add(currNode)
            
            for next_time, neighbor in adj[currNode]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (currTime + next_time, neighbor))
        
        return -1 if len(visited) < n else res
