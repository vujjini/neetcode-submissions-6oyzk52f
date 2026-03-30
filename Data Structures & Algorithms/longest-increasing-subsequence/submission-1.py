class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        seq = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
                continue
            l = 0
            r = len(seq) - 1
            swapPos = r
            while l <= r:
                m = (l + r) // 2
                if seq[m] == nums[i]:
                    swapPos = m
                    break
                elif seq[m] > nums[i]:
                    swapPos = m
                    r = m - 1
                else:
                    l = m + 1
            seq[swapPos] = nums[i]
        
        return len(seq)
