class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[-1] * nums[i - 1])

        right = [1 for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                right[i] = nums[i + 1] * right[i + 1]
        
        return [right[i] * left[i] for i in range(len(nums))]
        
        