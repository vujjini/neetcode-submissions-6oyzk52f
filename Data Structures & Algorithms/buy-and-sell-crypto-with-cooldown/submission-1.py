class Solution:
    def dfs(self, i, buy):
        if i >= len(self.prices):
            return 0

        if (i, buy) in self.dp:
            return self.dp[(i, buy)]
        
        cooldown = self.dfs(i + 1, buy)
        if buy:
            self.dp[(i, buy)] = max(self.dfs(i + 1, not buy) - self.prices[i], cooldown)
            return self.dp[(i, buy)]
        else:
            self.dp[(i, buy)] = max(self.dfs(i + 2, not buy) + self.prices[i], cooldown)
            return self.dp[(i, buy)]

    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}
        self.prices = prices
        return self.dfs(0, True)