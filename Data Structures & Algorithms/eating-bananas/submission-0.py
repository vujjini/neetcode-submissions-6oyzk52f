import math

class Solution:
    def calc_hrs(self, piles, k, h):
        res = 0
        for pile in piles:
            res+=(math.ceil(pile/k))
        return res <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            if self.calc_hrs(piles, m, h):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res