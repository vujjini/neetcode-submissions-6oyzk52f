class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a != 0:
            maxHeap.append((-a, 'a'))
        if b != 0:
            maxHeap.append((-b, 'b'))
        if c != 0:
            maxHeap.append((-c, 'c'))
        if len(maxHeap) == 0:
            return ""
        heapq.heapify(maxHeap)

        output = ""
# c = -5, b = -1             ccbccc
        while maxHeap:
            first = heapq.heappop(maxHeap)
            if output and output[-1] == first[1]:
                continue
            
            output+=first[1]
            if first[0] != -1:
                heapq.heappush(maxHeap, (first[0] + 1, first[1]))
            second = None
            if maxHeap:
                second = heapq.heappop(maxHeap)
                output+=second[1]
            
            if maxHeap:
                third = heapq.heappop(maxHeap)
                output+=third[1]
                if third[0] != -1:
                    heapq.heappush(maxHeap, (third[0] + 1, third[1]))
            
            if second and second[0] != -1:
                heapq.heappush(maxHeap, (second[0] + 1, second[1]))
        return output


