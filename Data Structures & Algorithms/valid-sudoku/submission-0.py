class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        print("row")
                        return False
                    s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        print("col")
                        print(board[i][j])
                        return False
                    s.add(board[j][i])
        x = {}
        for i in range(9):
            for j in range(9):
                pair = (i // 3, j // 3)
                if board[i][j] != '.':
                    if pair in x:
                        if board[i][j] in x[pair]:
                            print("ya")
                            return False
                        x[pair].add(board[i][j])
                    else:
                        x[pair] = {board[i][j]}
        return True

