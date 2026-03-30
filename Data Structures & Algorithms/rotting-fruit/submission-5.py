class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # keep track of number of fresh fruits
        # do BFS on the nodes level by level (only level at a time instead of continually processing nodes sequentially)
        # at any point in the BFS, all rotten nodes in the graph at the beginning of teh while loop are in same level
        # this ensures all nodes in the same level move simultaneosuly


        fresh = 0
        q = deque()
        visited = set()
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            curr_rotten = len(q)
            if fresh == 0:
                return res
            
            for i in range(curr_rotten):
                top = q.popleft()
                row = top[0]
                col = top[1]

                if row < len(grid) - 1 and (row + 1, col) not in visited and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    fresh-=1
                    q.append((row + 1, col))
                    visited.add((row + 1, col))
                if row > 0 and (row - 1, col) not in visited and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    fresh-=1
                    q.append((row - 1, col))
                    visited.add((row - 1, col))
                if col < len(grid[0]) - 1 and (row, col + 1) not in visited and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    fresh-=1
                    q.append((row, col + 1))
                    visited.add((row, col + 1))
                if col > 0 and (row, col - 1) not in visited and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    fresh-=1
                    q.append((row, col - 1))
                    visited.add((row, col - 1))
            res+=1

        return res if fresh == 0 else -1



                                

