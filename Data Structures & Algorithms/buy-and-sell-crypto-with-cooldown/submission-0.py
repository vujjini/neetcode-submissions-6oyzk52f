class Solution:
    def dfs(self, i, buy):
        if i >= len(self.prices):
            return 0
        
        cooldown = self.dfs(i + 1, buy)
        if buy:
            return max(self.dfs(i + 1, not buy) - self.prices[i], cooldown)
        else:
            return max(self.dfs(i + 2, not buy) + self.prices[i], cooldown)

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices

        return self.dfs(0, True)