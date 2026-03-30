import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        currTime = 0
        pq = [(-count, 0) for count in Counter(tasks).values()]
        heapq.heapify(pq)

        idle = deque()

        while pq or idle :
            if idle and idle[0][1] <= currTime:
                heapq.heappush(pq, idle.popleft())
            if pq:
                negFreq, minTime = heapq.heappop(pq)
                if negFreq < -1:
                    idle.append((negFreq + 1, currTime + n + 1))
            currTime+=1
        
        return currTime

        # []

        # [(-2, 4)]