class Solution:

    def bfs(self, i, j):
        if min(i, j) < 0 or i == self.m or j == self.n or self.grid[i][j] == 0 or self.grid[i][j] == 2:
            return
        self.q.append((i, j))
        self.total_rotten+=1
        self.grid[i][j] = 2


    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count the total number of fruits and number of rotten fruits
        # add all rotten fruits to the queue
        # do a BFS on each rotten fruit in the queue one by one and for each rotten fruit add its adjcents to the queue and change their state
        # keep incrementing the number of rotten fruits in each BFS call and in each iteration of the queue, increment the minutes
        # after the q becomes empty, if the number of rotten fruits == total number of fruits return the minutes else -1
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        total = 0
        self.total_rotten = 0
        self.q = deque()
        minutes = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    total+=1
                elif grid[i][j] == 2:
                    total+=1
                    self.total_rotten+=1
                    self.q.append((i, j))
        if total == 0:
            return 0

        while self.q:
            if self.total_rotten == total:
                return minutes
            for _ in range(len(self.q)):
                rotten = self.q.popleft()
                i, j = rotten[0], rotten[1]
                self.bfs(i + 1, j)
                self.bfs(i - 1, j)
                self.bfs(i, j + 1)
                self.bfs(i, j - 1)
            minutes+=1

        return -1
                