class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, s, visited):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited:
                return
            s_copy = s[:]
            s_copy+=board[i][j]
            visited.add((i, j))
            if s_copy == word:
                return True
            for x, y in dirs:
                if dfs(i + x, j + y, s_copy, visited):
                    return True
            visited.remove((i, j))
            return False
            

        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if dfs(i, j, "", visited):
                    return True
        
        return False