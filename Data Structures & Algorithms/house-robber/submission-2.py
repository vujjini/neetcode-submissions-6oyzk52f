class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for num in range(2, len(nums)):
            tmp = max(nums[num] + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return max(rob1, rob2)