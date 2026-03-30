class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m = set(nums)
        visited = set()

        res = 0

        for num in nums:
            if num in visited:
                continue
            curr_seq = 1
            next_num = num + 1
            while next_num in m:
                visited.add(next_num)
                curr_seq+=1
                next_num+=1
            res = max(res, curr_seq)
        
        return res