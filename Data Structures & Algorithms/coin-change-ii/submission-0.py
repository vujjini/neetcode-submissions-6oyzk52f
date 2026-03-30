class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[j for j in range(amount + 1)] for i in range(len(coins))]

        for i in range(len(coins)):
            # if i == 0:
            #     for j in range(1, amount + 1):
            #         dp[i][j] = 0
            #     continue
            dp[i][0] = 1

        for i in range(len(coins)):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j] if i > 0 else 0
                if j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]]
            
        
        return dp[len(coins) - 1][amount]

