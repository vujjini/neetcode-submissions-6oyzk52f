class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = Counter(tasks)
        maxHeap = [-m[task] for task in m]
        heapq.heapify(maxHeap)
        q = deque()
        curr_time = 0
        while maxHeap or q:
            curr_time+=1
            if q:
                curr_standby_time = curr_time - q[0][1]
                if curr_standby_time > n:
                    standby = q.popleft()
                    heapq.heappush(maxHeap, -standby[0])
            if not maxHeap:
                continue
            curr_task = heapq.heappop(maxHeap)
            if -curr_task > 1:
                q.append((-curr_task - 1, curr_time))
        
        return curr_time

