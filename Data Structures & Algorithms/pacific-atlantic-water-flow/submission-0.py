class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # do bfs on each node in the graph twice one for pacific and one for atlantic (1 / 0 filled 2d arrays) and then loop through them to find double 1s or just
        # in the second bfs check if first one also one at that index

        def flow_p(prev, i, j):
            if min(i, j) <= 0 or i >= m or j >= n or pacific[i][j] == 1 or heights[i][j] < heights[prev[0]][prev[1]]:
                return
            q.append([i, j])
            pacific[i][j] = 1
        
        def flow_a(prev, i, j):
            if min(i, j) < 0 or i >= m - 1 or j >= n - 1 or atlantic[i][j] == 1 or heights[i][j] < heights[prev[0]][prev[1]]:
                return
            q.append([i, j])
            atlantic[i][j] = 1

        q = deque()
        m = len(heights)
        n = len(heights[0])
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        res = []

        for i in range(m):
            pacific[i][0] = 1
            q.append([i, 0])
        for j in range(n):
            pacific[0][j] = 1
            q.append([0, j])
        

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i, j = curr[0], curr[1]
                flow_p(curr, i + 1, j)
                flow_p(curr, i - 1, j)
                flow_p(curr, i, j + 1)
                flow_p(curr, i, j - 1)

        q = deque()
        atlantic = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            atlantic[i][n - 1] = 1
            q.append([i, n - 1])
        for j in range(n):
            atlantic[m - 1][j] = 1
            q.append([m - 1, j])
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i, j = curr[0], curr[1]
                flow_a(curr, i + 1, j)
                flow_a(curr, i - 1, j)
                flow_a(curr, i, j + 1)
                flow_a(curr, i, j - 1)

        for i in range(m):
            for j in range(n):
                if pacific[i][j]*atlantic[i][j] == 1:
                    res.append([i, j])

        return res



        
        
        