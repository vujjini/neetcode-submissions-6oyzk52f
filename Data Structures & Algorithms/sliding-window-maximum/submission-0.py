class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # maintain a maxHeap of size k
        # once size k is reached:
        # update global max with currMax ony if its index is >= left pointer
        # slide the window by popping from the maxHeap and pushing the new value into it
        # it doesn't matter whether the max we popped exists in the new window as:
        #   the global max already has the max value
        #   we only change global max when the new value entered is greater than global max
        #   in that case, the new value will anyway be the max of the heap

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
        
        # [(2, 1), (1, 0), (1, 2)]
        # [2, 2, ]
            
        return res
            


        

        