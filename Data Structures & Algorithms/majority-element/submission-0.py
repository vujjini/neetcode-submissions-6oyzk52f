class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        half = len(nums) // 2

        for num in count:
            if count[num] > half:
                return num