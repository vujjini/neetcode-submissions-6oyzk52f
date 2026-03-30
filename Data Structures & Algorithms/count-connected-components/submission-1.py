class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0

        adj = {}

        for i in range(n):
            adj[i] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def bfs(node, visited):
            visited.add(node)
            q = deque()
            q.append(node)

            while q:
                top = q.popleft()
                for neighbor in adj[top]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        visited = set()
        for node in adj:
            if node not in visited:
                res+=1
                bfs(node, visited)
        
        return res