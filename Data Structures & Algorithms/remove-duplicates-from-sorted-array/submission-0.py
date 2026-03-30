class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = i + 1
        res = 1

        while j < len(nums):
            
            while j < len(nums) and nums[j] == nums[i]:
                j+=1
            if j > len(nums) - 1:
                break

            nums[i + 1] = nums[j]
            i+=1
            j+=1
            res+=1
        
        return res

# [1, 2, 3, 3, 4]