class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False
        
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, visited, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited, node):
                        return True
                elif neighbor != parent:
                    return True
        
            return False
        
        visited = set()


        cycle = dfs(0, visited, -1)
        if cycle:
            return False

        if len(visited) < len(adj):
            return False

        return True


        
