class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        curr_span = 1
        while self.st and self.st[-1][0] <= price:
            curr_span+=self.st[-1][1]
            self.st.pop()
        self.st.append((price, curr_span))

        return curr_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)