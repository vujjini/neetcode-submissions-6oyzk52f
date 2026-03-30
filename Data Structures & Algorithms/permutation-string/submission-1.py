class Solution:
    def count(self, s):
        res = {}
        for i in s:
            if i in res:
                res[i]+=1
                continue
            res[i] = 1
        return res

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        left = 0
        for right in range(m - 1, n):
            curr_sub = s2[left:right + 1]
            if self.count(s1) != self.count(curr_sub):
                left+=1
                continue
            return True
        
        return False
            
