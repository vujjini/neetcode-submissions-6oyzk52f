class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS, n = len(board), len(board[0]), len(word)
        visited = set()
        
        def dfs(r, c, i):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or i >= n or board[r][c] != word[i]:
                return False
            if i == n - 1 and word[i] == board[r][c]:
                return True
            visited.add((r, c))

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            visited.remove((r, c))

            return res
        

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        
        return False

            

        