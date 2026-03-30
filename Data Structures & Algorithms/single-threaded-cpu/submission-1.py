class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [2, 1, 3], [3, 3, 4], [4, 1, 2], [4, 4, 1], [5, 2, 0]
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort(key = lambda item: item[0])
        res = []
        i = 0
        t = tasks[0][0]
        minHeap = []
        while i < len(tasks):
            j = i
            while j < len(tasks) and tasks[j][0] <= t:
                heapq.heappush(minHeap, (tasks[j][1], tasks[j][2]))
                j+=1
            if j == i:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                j+=1
            popped = heapq.heappop(minHeap)
            t+=popped[0]
            res.append(popped[1])
            i = j
        
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])

        return res
            
        