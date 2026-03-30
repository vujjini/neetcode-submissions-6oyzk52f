class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(i, j):
            if ((i, j) in visited or i < 0 or j < 0 or 
            i >= ROWS or j >= COLS or board[i][j] != 'O'):
                return
            board[i][j] = 'T'
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        

        
                
