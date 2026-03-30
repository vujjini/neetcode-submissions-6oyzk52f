class Solution:

    def bfs(self, source, adj):

        q = deque()
        q.append(source)

        while q:
            curr = q.popleft()
            self.island_len+=1
            for adjacent in adj[curr]:
                if adjacent not in self.visited:
                    q.append(adjacent)
                    self.visited.add(adjacent)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = {}

        n = 0
        for i in range(len(grid)):
            for j in range((len(grid[i]))):
                if grid[i][j] == 1:
                    m[(i, j)] = n
                    n+=1
            
        adj = {node: [] for node in range(len(m))}

        for coords in m:
            x = coords[0]
            y = coords[1]
            if x > 0 and grid[x - 1][y] == 1:
                adj[m[coords]].append(m[(x - 1, y)])
            if y > 0 and grid[x][y - 1] == 1:
                adj[m[coords]].append(m[(x, y - 1)])
            if x < len(grid) - 1 and grid[x + 1][y] == 1:
                adj[m[coords]].append(m[(x + 1, y)])
            if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
                adj[m[coords]].append(m[(x, y + 1)])
        
        self.visited = set()

        res = 0
        for node in adj:
            if node not in self.visited:
                self.island_len = 0
                self.visited.add(node)
                self.bfs(node, adj)
                res = max(res, self.island_len)
        
        return res
                