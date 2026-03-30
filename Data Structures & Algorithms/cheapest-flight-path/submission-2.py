class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for flight in flights:
            adj[flight[0]].append((flight[2], flight[1]))

        # Use a queue for BFS-style traversal instead of minHeap
        queue = deque([(0, src)])

        prices = [float('inf') for i in range(n)]
        prices[src] = 0

        stops = 0
        while queue and stops <= k:
            size = len(queue)
            for _ in range(size):
                currPrice, currNode = queue.popleft()

                for nextPrice, neighbor in adj[currNode]:
                    newPrice = currPrice + nextPrice
                    if newPrice < prices[neighbor]:
                        prices[neighbor] = newPrice
                        queue.append((newPrice, neighbor))
            stops += 1

        return -1 if prices[dst] == float("inf") else prices[dst]