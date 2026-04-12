class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        q = deque()
        for node in adj:
            if len(adj[node]) == 1:
                q.append(node)
        
        while q:
            top = q.pop()
            for neighbor in adj[top]:
                adj[neighbor].remove(top)
                if len(adj[neighbor]) == 1:
                    q.append(neighbor)
            adj.pop(top)
        for u, v in reversed(edges):
            if u in adj and v in adj:
                return [u, v]
        
