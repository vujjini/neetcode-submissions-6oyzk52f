class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checker = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in checker:
                return [checker[diff], i]
            
            if nums[i] not in checker:
                checker[nums[i]] = i
            
        