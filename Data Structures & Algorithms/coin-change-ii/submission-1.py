class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        cache = {}

        def dp(i, change):
            
            if (i, change) in cache:
                return cache[(i, change)]
            if i >= len(coins) or change < 0:
                return 0

            if change == 0:
                cache[(i, change)] = 1
            else:
                cache[(i, change)] = dp(i + 1, change) + dp(i, change - coins[i])
            
            return cache[(i, change)]
        
        return dp(0, amount)

            
