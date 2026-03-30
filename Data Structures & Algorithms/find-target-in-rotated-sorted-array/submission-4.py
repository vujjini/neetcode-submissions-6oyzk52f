class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if left half is sorted and if target exists in it, if so go there else go right, if left is not sorted, check 

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1