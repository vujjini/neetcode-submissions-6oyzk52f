class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.adj = {}
        self.res = 0
        self.visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                self.adj[(i, j)] = []
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    self.adj[(i, j)].append((i + 1, j))
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    self.adj[(i, j)].append((i, j + 1))
                if i > 0 and grid[i - 1][j] == 1:
                    self.adj[(i, j)].append((i - 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    self.adj[(i, j)].append((i, j - 1))
        
        def bfs(source):
            q = deque()
            q.append(source)
            self.visited.add(source)
            area = 1

            while q:
                top = q.popleft()
                for neighbour in self.adj[top]:
                    if neighbour not in self.visited:
                        area+=1
                        q.append(neighbour)
                        self.visited.add(neighbour)

            self.res = max(self.res, area)
        
        for source in self.adj:
            if source not in self.visited:
                bfs(source)
        
        return self.res


                