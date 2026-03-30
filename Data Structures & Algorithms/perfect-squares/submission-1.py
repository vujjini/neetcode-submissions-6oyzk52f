class Solution:
    def numSquares(self, n: int) -> int:

        dp = [-1 for i in range(n + 1)]
        def dfs(s):
            if dp[s] != -1:
                return dp[s]
            if s == 0:
                return 0
            res = s
            for i in range(1, s):
                if i*i > s:
                    break
                res = min(res, 1 + dfs(s - i*i))
            dp[s] = res
            return dp[s]
        
        return dfs(n) 