class Solution:
    def reverse(self, nums, i, j):
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i+=1
            j-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0:
            return
        self.reverse(nums, 0, len(nums) - 1)


        self.reverse(nums, 0, k - 1)
        print(nums)
        self.reverse(nums, k, len(nums) - 1)
        print(nums)
