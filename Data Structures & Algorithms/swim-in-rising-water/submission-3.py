class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        dist = {}

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while minHeap:
            currTime, i, j = heapq.heappop(minHeap)
            if (i, j) in visited:
                continue
            dist[(i, j)] = currTime
            visited.add((i, j))
            
            if i == ROWS - 1 and j == COLS - 1:
                return currTime

            for move in dirs:
                neighbor = (i + move[0], j + move[1])
                if (neighbor in visited or neighbor[0] < 0 or neighbor[0] >= ROWS or
                neighbor[1] < 0 or neighbor[1] >= COLS):
                    continue
                
                nextTime = max(currTime, grid[neighbor[0]][neighbor[1]])
                heapq.heappush(minHeap, (nextTime, neighbor[0], neighbor[1]))
        
        print(dist)
        return dist[(ROWS - 1, COLS - 1)]