class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        rob = [0 for i in range(len(nums))]

        rob[0], rob[1] = nums[0], max(nums[0], nums[1])

        for num in range(2, len(nums)):
            rob[num] = max(nums[num] + rob[num - 2], rob[num - 1])
        
        return max(rob[-1], rob[-2])