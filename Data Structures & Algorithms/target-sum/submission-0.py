class Solution:
    
    def find_ways(self, i, curr_value):
        if i == len(self.nums):
            return 0 if curr_value != self.target else 1
        if (i, curr_value) in self.dp:
            return self.dp[(i, curr_value)]

        self.dp[(i, curr_value)] = self.find_ways(i + 1, curr_value + self.nums[i - 1]) + self.find_ways(i + 1, curr_value - self.nums[i - 1])

        return self.dp[(i, curr_value)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.dp = {}
        self.nums = nums
        self.target = target
        
        return self.find_ways(0, 0)
        
