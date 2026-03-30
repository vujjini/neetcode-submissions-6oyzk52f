class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add the chests in a queue
        # while q is not empty, loop through the queue in a bfs fashion level by level
        land = 2147483647
        water = -1
        chest = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == chest:
                    q.append([i, j])
        visited = set()
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i, j = curr[0], curr[1]
                if i + 1 < len(grid) and grid[i + 1][j] == land:
                    q.append([i + 1, j])
                    grid[i + 1][j] = grid[i][j] + 1
                if j + 1 < len(grid[0]):
                    if grid[i][j + 1] == land:
                        q.append([i, j + 1])
                        grid[i][j + 1] = grid[i][j] + 1
                if i - 1 >= 0 and grid[i - 1][j] == land:
                    q.append([i - 1, j])
                    grid[i - 1][j] = grid[i][j] + 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == land: 
                        q.append([i, j - 1])
                        grid[i][j - 1] = grid[i][j] + 1