class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        prods = [(1, 1)]

        for i in range(0, len(nums)):
            if nums[i] == 0:
                prods.append((1, 1))
                res = max(res, 0)
                continue
            elif nums[i] < 0:
                currMax, currMin = max(nums[i], prods[-1][1]*nums[i]), min(nums[i], prods[-1][0]*nums[i])
            else:
                currMax, currMin = max(nums[i], prods[-1][0]*nums[i]), min(nums[i], prods[- 1][1]*nums[i])
            res = max(res, currMax)
            prods.append((currMax, currMin))
        
        return res