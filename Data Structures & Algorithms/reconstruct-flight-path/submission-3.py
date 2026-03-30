import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(node):
            while adj[node]:
                nei = heapq.heappop(adj[node])
                dfs(nei)
            res.append(node)

        dfs("JFK")

        return res[::-1]