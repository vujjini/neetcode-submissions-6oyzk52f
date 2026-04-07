class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # [1, 20], [2, 10], [3, 5], [4, 9], [6, 8]
        # []

        # [(20, 0), (10, 2), (12, 1)]

        counts = defaultdict(int)
        rooms = [i for i in range(n)]
        endTimes = []
        meetings.sort()

        for currStart, currEnd in meetings:
            duration = currEnd - currStart
            while endTimes and endTimes[0][0] <= currStart:
                _, room = heapq.heappop(endTimes)
                heapq.heappush(rooms, room)
            if not rooms:
                start, currRoom = heapq.heappop(endTimes)
            else:
                start, currRoom = currStart, heapq.heappop(rooms)
            heapq.heappush(endTimes, (start + duration, currRoom))
            counts[currRoom]+=1
        
        res, maxCount = 0, 1
        for room in counts:
            if counts[room] > maxCount:
                res, maxCount = room, counts[room]
        print(counts)
        return res