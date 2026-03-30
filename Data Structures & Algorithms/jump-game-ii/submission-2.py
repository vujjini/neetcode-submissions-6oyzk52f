# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums)
#         i = 0
#         while i < n:
#             if i == n - 1:
#                 return res
#             next_step = i + 1
#             for j in range(2, nums[i] + 1):
#                 if i + j >= n - 1:
#                     next_step = i + j
#                     break
#                 if nums[i + j] >= nums[next_step]:
#                     next_step = i + j
#             i = next_step
#             res+=1
        
#         return res

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        end = 0
        farthest = 0

        # we stop at n - 2, because once we reach last index we don’t need more jumps
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                res += 1
                end = farthest

        return res
