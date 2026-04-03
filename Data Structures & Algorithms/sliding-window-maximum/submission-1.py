class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # maintain a maxHeap of size k
        # once size k is reached:

        l = 0
        maxHeap = []
        res = []

        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if len(maxHeap) < k:
                continue
            currMax, currIdx = heapq.heappop(maxHeap)
            while maxHeap and currIdx < l:
                currMax, currIdx = heapq.heappop(maxHeap)
            if currIdx >= l:
                res.append(-currMax)
                heapq.heappush(maxHeap, (currMax, currIdx))
            l+=1
        
            
        return res
            


        

        