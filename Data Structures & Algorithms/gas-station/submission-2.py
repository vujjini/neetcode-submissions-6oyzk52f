class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        starting = 0
        total_surplus = 0

        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            if total_surplus < 0:
                starting = i + 1
                total_surplus = 0

        return starting