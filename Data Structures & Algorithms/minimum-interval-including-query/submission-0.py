class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        # sort intervals
        # we wanna find the shortest interval for each query
            # we use minHeap to store all intervals
            # first, pop from the minHeap, intervals with the end time < query
            # then add all the intervals it can possibly belong to
            # so add every start time <= query
            # add (length, endTime) so that for equal lens, lwoer endtime is popped first
        
        intervals.sort()
        minHeap = []
        i = 0
        res = {}
        
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

        