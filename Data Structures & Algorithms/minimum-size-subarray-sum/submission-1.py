class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = nums[0]
        if curr_sum >= target:
            return 1
        i = 0
        j = 1
        curr_min = 100001
        while j < len(nums):
            curr_sum+=nums[j]
            while curr_sum >= target and i <= j:
                curr_min = min(curr_min, j - i + 1)
                curr_sum-=nums[i]
                i+=1
            j+=1
        
        return curr_min if curr_min != 100001 else 0