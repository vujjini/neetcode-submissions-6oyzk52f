class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(o, c, currStr):
            if o == 0  and c == 0:
                res.append(currStr)
                return
            if o == 0:
                dfs(o, c - 1, currStr + ')')
                return
            elif o == c:
                dfs(o - 1, c, currStr + '(')
            else:
                dfs(o - 1, c, currStr + '(')
                dfs(o, c - 1, currStr + ')')

        dfs(n, n, "")
        
        return res