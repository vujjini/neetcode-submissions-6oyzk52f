class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, w, visited):
            if w == len(word):
                return True
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or board[i][j] != word[w]:
                return False
            visited.add((i, j))
            for x, y in dirs:
                if dfs(i + x, j + y, w + 1, visited):
                    return True
            visited.remove((i, j))
            return False
            

        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if dfs(i, j, 0, visited):
                    return True
        
        return False