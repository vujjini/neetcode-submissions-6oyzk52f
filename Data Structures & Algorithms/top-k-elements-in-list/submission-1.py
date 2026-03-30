class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        count = defaultdict(int)

        for num in nums:
            count[num]+=1
        
        for num in count:
            heapq.heappush(maxHeap, (-count[num], num))

        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res