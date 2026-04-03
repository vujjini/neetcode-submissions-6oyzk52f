class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

        # [-4, -3, -2] [-1]

    def addNum(self, num: int) -> None:
        if not self.right:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        while self.left and self.right[0] <= -self.left[0] or (len(self.left) - len(self.right) > 1):
            leftTop = -heapq.heappop(self.left)
            heapq.heappush(self.right, leftTop)
        
        while len(self.right) - len(self.left) > 1:
            rightTop = heapq.heappop(self.right)
            heapq.heappush(self.left, -rightTop)

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

# maintain two heaps (left and right)
# add the number to left
# if the difference b/w left and right becomes greater than 1
# pop from left and add it to right

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()