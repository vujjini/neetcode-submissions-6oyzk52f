class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        last_visited = -1
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                last_visited+=1
                nums[last_visited] = nums[i]
                k+=1
        
        return k