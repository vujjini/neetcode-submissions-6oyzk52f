class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        outer_visited = set()
        for i in range(len(nums)):
            if nums[i] in outer_visited:
                continue
            curr_target = target - nums[i]

            # run a 3sum algorithm
            visited = set()
            for j in range(i + 1, len(nums)):
                if nums[j] in visited:
                    continue
                sumTo = curr_target - nums[j]
                k, l = j + 1, len(nums) - 1
                while k < l:
                    if nums[k] + nums[l] == sumTo:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif nums[k] + nums[l] < sumTo:
                        k+=1
                    else:
                        l-=1
                visited.add(nums[j])
            outer_visited.add(nums[i])
        return res
