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
            while maxHeap and maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            currMax, currIdx = maxHeap[0]
            res.append(-currMax)
            l+=1
        
            
        return res
            


        

        