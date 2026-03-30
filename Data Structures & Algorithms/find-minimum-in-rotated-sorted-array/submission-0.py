class Solution:
    def findMin(self, nums: List[int]) -> int:
        # do a bianry search in which we always check the half with the pivot
        # if the array is not sorted we know that there is a pivot in it and if we split it and the left portion is
        # sorted, we can assure that the right portion contains the pivot and if the left portion is not sorted, then the the left contains
        # the pivot. We go where the pivot exists and when teh current array is found to be sorted, instead of splitting again, we just
        # set the minimum to the leftmost element

        l = 0
        r = len(nums) - 1
        res = 1001
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res
            
                