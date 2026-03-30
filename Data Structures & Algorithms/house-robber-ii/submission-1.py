class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        rob1 = [-1 for i in range(len(nums) - 1)]
        rob2 = [-1 for i in range(len(nums) - 1)]

        def rec(i, rob, houses):
            if i >= len(houses):
                return 0
            if rob[i] != -1:
                return rob[i]
            rob[i] = max(rec(i + 1, rob, houses), houses[i] + rec(i + 2, rob, houses))

            return rob[i]
        
        return max(rec(0, rob1, nums[:-1]), rec(0, rob2, nums[1:])) 

        # rec(i) = max(rec(i + 1), nums[i] + nums(i + 2))