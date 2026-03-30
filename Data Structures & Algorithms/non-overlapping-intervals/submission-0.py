class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1, 3], [2, 2], [2, 3], [3, 4]
        # [2, 2], [2, 3], [3, 4]

        intervals.sort(key=lambda x: x[1])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
        
        return len(intervals) - len(res)