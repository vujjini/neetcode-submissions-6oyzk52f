"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x: x.start)
        res = 1

        # [(2, 6), (3, 7), (4, 8)]

        currMeets = []

        for i in range(0, len(intervals)):
            print(currMeets)
            while currMeets and currMeets[0] <= intervals[i].start:
                heapq.heappop(currMeets)
            heapq.heappush(currMeets, intervals[i].end)
            res = max(res, len(currMeets))
        
        return res



        