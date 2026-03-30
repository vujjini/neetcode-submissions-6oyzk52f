class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def dfs(i, currSet):

            if i >= len(nums):
                res.add(tuple(currSet))
                return
            
            currSet.append(nums[i])
            dfs(i + 1, currSet)
            currSet.pop()
            dfs(i + 1, currSet)

        dfs(0, [])

        return [list(subset) for subset in res] 