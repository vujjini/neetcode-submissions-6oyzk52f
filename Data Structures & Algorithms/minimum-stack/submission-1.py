class MinStack:

    def __init__(self):
        self.l = []
        self.m = []
        

    def push(self, val: int) -> None:
        if len(self.m) > 0:
            # if we have a new minimum
            if val <= self.m[-1]:
                self.m.append(val)
        else:
            self.m.append(val)
        self.l.append(val)
        


        return None

    def pop(self) -> None:
        t = self.l[-1]
        self.l.pop()
        if t == self.m[-1]:
            self.m.pop()
        
        pass

    def top(self) -> int:
        return self.l[-1]


    def getMin(self) -> int:
        return self.m[-1]
        
