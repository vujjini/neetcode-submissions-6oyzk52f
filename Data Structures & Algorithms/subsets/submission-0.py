class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # []
        # [1] []
        # [1, 2] [1]

        res = [[]]

        def dfs(i, subset):
            if i == len(nums):
                return
            subset.append(nums[i])
            res.append(subset[:])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])

        return res

        # [[], [1], [1, 2]]

        # [1, 2]