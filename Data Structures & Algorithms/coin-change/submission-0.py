class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # 12

        # (i, sum)

        # rec(i, sum) = 1 + min(rec(i + 1, sum), rec(i, sum + coins[i]))

        # if sum == 0:
        #   return 1
        # if sum < 0:
        #   return inf

        # [1, 5, 10]

        # [1 (3), 1 (2), 5(2), 5 (1), ]
        #               , 10(1)

        # [1, 5, 10]  sum = 0
        cache = {}

        def dp(i, s):
            if (i, s) in cache:
                return cache[(i, s)]
            
            if i < 0 or s < 0:
                return float('inf')
            elif s == 0:
                cache[(i, s)] = 0
            else:
                cache[(i, s)] = min(dp(i - 1, s), 1 + dp(i, s - coins[i]))

            return cache[(i, s)]
        
        
        res = dp(len(coins) - 1, amount)

        return -1 if res == float('inf') else res

