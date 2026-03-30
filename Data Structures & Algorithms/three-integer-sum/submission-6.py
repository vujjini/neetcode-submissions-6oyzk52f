class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        for curr in range(len(nums)):
            if nums[curr] in visited:
                continue
            curr_val = -nums[curr]
            i = curr + 1
            j = len(nums) - 1
            while i < j:
                two_sum = nums[i] + nums[j]
                if two_sum == curr_val:
                    res.append([nums[curr], nums[i], nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i - 1]:
                        i+=1
                    while i < j and nums[j] == nums[j + 1]:
                        j-=1
                elif two_sum > curr_val:
                    j-=1
                else:
                    i+=1
            visited.add(nums[curr])
        
        return res