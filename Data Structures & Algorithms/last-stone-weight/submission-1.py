class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -stones[0]
            heapq.heappop(stones)
            y = -stones[0]
            heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, -(x - y))
        
        return -stones[0] if len(stones) > 0 else 0