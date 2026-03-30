class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = len(nums) - 1
        for j in range(len(nums) - 2, -1, -1):
            curr_diff = i - j
            if nums[j] >= curr_diff:
                if j == 0:
                    return True
                i = j
        
        return False