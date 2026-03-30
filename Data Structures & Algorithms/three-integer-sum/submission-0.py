class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        print(nums)
        for x in range(len(nums)):
            if x != 0 and nums[x] == nums[x - 1]:
                continue
            i = x + 1
            j = len(nums) - 1
            while i < j:
                if i != x + 1 and nums[i] == nums[i - 1]:
                    i+=1
                    continue
                if j != len(nums) - 1 and nums[j] == nums[j+1]:
                    j-=1
                    continue
                if i >= j:
                    break
                s = nums[i] + nums[j] + nums[x]
                if s == 0:
                    l.append([nums[x], nums[i], nums[j]])
                    i+=1
                    j-=1
                elif s < 0:
                    i+=1
                else:
                    j-=1
        return l
        