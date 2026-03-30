class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif mid > 0 and nums[left] <= nums[mid - 1]: # left side is sorted
                if target >= nums[left] and target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid < len(nums) - 1 and target >= nums[mid + 1] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
            