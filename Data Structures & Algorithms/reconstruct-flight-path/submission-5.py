import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # create an adj list except have a PQ instead of list

        adj = defaultdict(list)

        for ticket in tickets:
            heapq.heappush(adj[ticket[0]], ticket[1])
        
        # Prioritze based on lexicographic score -> O(1) time complex (3 operations for each)
        # time complexity to enqueue and deqeue -> O(log n)
        # time complexity to build the list -> O(nlogn / 2) -> O(nlogn)
        # what about cycles? If no cycles present, below alg works
        # Start with JFK as source
        # dfs(node, res):
        #   for each neighbor of the node (already in order):
        #       add it to res
        #       dfs(neighbor, res)
        def dfs(node, res):
            while adj[node]:
                top = heapq.heappop(adj[node])
                dfs(top, res)
            res.append(node)
        
        res = []
        dfs("JFK", res)

        return res[::-1]

        
        # JFK = []