class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        res = 0
        
        for origin in range(len(nums)):
            swap = origin
            while swap < len(nums) and nums[swap] == val:
                swap+=1
            if swap >= len(nums):
                break
            tmp = nums[origin]
            nums[origin] = nums[swap]
            nums[swap] = tmp
            res+=1
        
        return res

