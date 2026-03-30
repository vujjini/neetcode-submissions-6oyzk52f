"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        i, j = 0, 0
        res = 0
        while i < len(starts) and j < len(ends):
            if starts[i] < ends[j]:
                res+=1
                i+=1
            else:
                i+=1
                j+=1
        
        return res