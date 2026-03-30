class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # cost(i) = min(cost(i + 1), cost(i + 2))
        # cost(0)

        costs = [-1 for i in range(len(cost))]

        def dp(step):
            if step > len(cost) - 1:
                return 0
            if costs[step] != -1:
                return costs[step]
            costs[step] = cost[step] + min(dp(step + 1), dp(step + 2))

            return costs[step]
        
        return min(dp(0), dp(1))