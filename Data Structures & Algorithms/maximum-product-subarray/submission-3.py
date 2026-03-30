class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        currMax, currMin = 1, 1

        for i in range(0, len(nums)):
            prevMax, prevMin = currMax, currMin
            if nums[i] == 0:
                currMax, currMin = 1, 1
                res = max(res, 0)
                continue
            elif nums[i] < 0:
                currMax, currMin = max(nums[i], prevMin*nums[i]), min(nums[i], prevMax*nums[i])
            else:
                currMax, currMin = max(nums[i], prevMax*nums[i]), min(nums[i], prevMin*nums[i])
            res = max(res, currMax)
            # prods.append((currMax, currMin))
        
        return res