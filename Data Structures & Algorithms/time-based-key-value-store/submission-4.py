class TimeMap:

    def __init__(self):
        
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.mp[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if not self.mp[key] or timestamp < self.mp[key][0][0]:
            return ""
        
        recent = 0
        l = 0
        r = len(self.mp[key]) - 1

        while l <= r:
            m = (l + r) // 2
            if timestamp == self.mp[key][m][0]:
                return self.mp[key][m][1]
            elif self.mp[key][m][0] < timestamp:
                recent = m
                l = m + 1
            else:
                r = m - 1
        
        return self.mp[key][recent][1]
