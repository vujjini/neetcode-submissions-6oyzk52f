class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]

        res = set()

        nums.sort()

        for i in range(len(nums)):
            if i != 0:
                if nums[i] == prev:
                    continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == -(nums[i]):
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < -(nums[i]):
                    j+=1
                else:
                    k-=1
                
            prev = nums[i]

        return [list(ans) for ans in res]