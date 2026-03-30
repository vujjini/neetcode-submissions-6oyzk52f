class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append((value, timestamp))
            return
        self.m[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        l = 0
        r = len(self.m[key]) - 1
        res = ""
        if self.m[key][-1][1] <= timestamp:
            return self.m[key][-1][0]
        while l <= r:
            m = (l + r) // 2
            if timestamp == self.m[key][m][1]:
                return self.m[key][m][0]
            elif timestamp < self.m[key][m][1]:
                r = m - 1
            else:
                res = self.m[key][m][0]
                l = m + 1
        return res