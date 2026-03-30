class Solution:

    def bfs(self, source, adj):
        q = deque()
        q.append(source)
        while q:
            curr = q.pop()
            for adj_node in adj[curr]:
                if adj_node not in self.visited:
                    q.append(adj_node)
                    self.visited.add(adj_node)


    def numIslands(self, grid: List[List[str]]) -> int:
        # first ill create a map mapping all the co ordinates of each node to an integer starting from 0
        # then ill create an adjacency list mapping each node to its adjacenct nodes
            # ill iterate through the matrix, for each [i][j], if its equal to 1, ill map adjacent 1s
        # apply BFS

        m = {}
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    m[(i, j)] = n
                    n+=1
        
        adj = {m[node]: [] for node in m}

        for node in m:
            x = node[0]
            y = node[1]
            if x > 0 and grid[x - 1][y] == '1':
                adj[m[node]].append(m[(x - 1, y)])
            if y > 0 and grid[x][y - 1] == '1':
                adj[m[node]].append(m[(x, y - 1)])
            if x < len(grid) - 1 and grid[x + 1][y] == '1':
                adj[m[node]].append(m[(x + 1, y)])
            if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
                adj[m[node]].append(m[(x, y + 1)])
        
        
        self.visited = set()
        res = 0
        for node in adj:
            if node not in self.visited:
                self.visited.add(node)
                self.bfs(node, adj)
                res+=1
        
        return res

