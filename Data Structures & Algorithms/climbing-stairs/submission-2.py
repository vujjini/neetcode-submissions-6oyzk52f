class Solution:
    def climbStairs(self, n: int) -> int:

        ways = [-1 for i in range(n + 1)]
        # [-1, -1, -1]
        
        def rec(currSteps):
            if currSteps > n:
                return 0
            elif ways[currSteps] != -1:
                return ways[currSteps]
            elif currSteps == n:
                ways[currSteps] = 1
            else:
                ways[currSteps] = rec(currSteps + 1) + rec(currSteps + 2)
            return ways[currSteps]
        
        return rec(0)