class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited:
                if abs(visited[nums[i]] - i) <= k:
                    return True
            visited[nums[i]] = i
        
        return False
            