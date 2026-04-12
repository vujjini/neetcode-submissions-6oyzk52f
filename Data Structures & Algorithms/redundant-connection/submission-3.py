class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        
        q = deque()
        for node in indegree:
            if indegree[node] == 1:
                q.append(node)
        
        while q:
            top = q.pop()
            for neighbor in adj[top]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 1:
                    q.append(neighbor)
            adj.pop(top)
        for u, v in reversed(edges):
            if u in adj and v in adj:
                return [u, v]
        
