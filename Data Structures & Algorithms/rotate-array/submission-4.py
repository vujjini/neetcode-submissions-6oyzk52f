class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            while i <= j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i+=1
                j-=1
        n = len(nums)

        r = k%n

        reverse(n - r, len(nums) - 1)
        reverse(0, n - r - 1)
        reverse(0, len(nums) - 1)

        return nums
            