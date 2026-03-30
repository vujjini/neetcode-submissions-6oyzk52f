class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob = [-1 for i in range(len(nums))]

        def dp(house):
            if house >= len(nums):
                return 0
            if rob[house] != -1:
                return rob[house]
            rob[house] = max(nums[house] + dp(house + 2), dp(house + 1))
    
            return rob[house]
        
        return max(dp(0), dp(1))