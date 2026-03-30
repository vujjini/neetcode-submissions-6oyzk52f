class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # there are 4 maximum possible moves from each treasure cell
        # run a BFS traversal from each treasure cell
        #   while doing so, update a neighbour's val with (4 max possible)
        #   by adding 1 to curr_node's val (initally the treasure cell)
        #   if and only if the neighbor is reachable, and if 1 + curr_node val is < existing val then update and add the neighbor to queue
        #   Do BFS for each treasure cell. empty visited each time

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited = set()
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j))
                    while q:
                        top = q.popleft()
                        row = top[0]
                        col = top[1]
                        updated_val = 1 + grid[row][col]
                        if (row + 1, col) not in visited:
                            if row < len(grid) - 1 and grid[row + 1][col] > 0 and updated_val < grid[row + 1][col]:
                                grid[row + 1][col] = updated_val
                                q.append((row + 1, col))
                                visited.add((row + 1, col))
                        if (row, col + 1) not in visited:
                            if col < len(grid[0]) - 1 and grid[row][col + 1] > 0 and updated_val < grid[row][col + 1]:
                                grid[row][col + 1] = updated_val
                                q.append((row, col + 1))
                                visited.add((row, col + 1))
                        if (row - 1, col) not in visited:
                            if row > 0 and grid[row - 1][col] > 0 and updated_val < grid[row - 1][col]:
                                grid[row - 1][col] = updated_val
                                q.append((row - 1, col))
                                visited.add((row - 1, col))
                        if (row, col - 1) not in visited:
                            if col > 0 and grid[row][col - 1] > 0 and updated_val < grid[row][col - 1]:
                                grid[row][col - 1] = updated_val
                                q.append((row, col - 1))
                                visited.add((row, col - 1))
                
        