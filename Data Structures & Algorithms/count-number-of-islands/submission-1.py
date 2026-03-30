class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if horizontally, vertically and diagonally
        # adj list: keys -> tuple(indices) and value = list of neighbour tuples
        # run a BFS on each vertex and increment counter for non visited vertices

        self.adj = {}
        self.visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                self.adj[(i, j)] = []
                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == "1":
                        self.adj[(i, j)].append((i, j + 1))
                if i < len(grid) - 1:
                    if grid[i + 1][j] == "1":
                        self.adj[(i, j)].append((i + 1, j))
                # if i < len(grid) - 1 and j < len(grid[0]) - 1:
                #     if grid[i + 1][j + 1] == "1":
                #         self.adj[(i, j)].append((i + 1, j + 1))
                if j > 0:
                    if grid[i][j - 1] == "1":
                        self.adj[(i, j)].append((i, j - 1))
                if i > 0:
                    if grid[i - 1][j] == "1":
                        self.adj[(i, j)].append((i - 1, j))
                # if i > 0 and j > 0:
                #     if grid[i - 1][j - 1] == "1":
                #         self.adj[(i, j)].append((i - 1, j - 1))

                
        def bfs(source):
            q = deque()
            q.append(source)
            self.visited.add(source)

            while q:
                top = q.popleft()
                for neighbour in self.adj[top]:
                    if neighbour not in self.visited:
                        q.append(neighbour)
                        self.visited.add(neighbour)
        
        res = 0
        for source in self.adj:
            if source not in self.visited:
                print(source)
                res+=1
                bfs(source)
        
        return res


