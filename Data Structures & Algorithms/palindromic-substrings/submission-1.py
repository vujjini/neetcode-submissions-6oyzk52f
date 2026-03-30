class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def subLen(l, r, res):
            
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res+=1
                    l-=1
                    r+=1
                else:
                    break
            
            return res
        
        res = 0

        # first pass
        for i in range(len(s)):
            l = i - 1
            r = i + 1

            res+=subLen(l, r, 1)

        
        for j in range(1, len(s)):
            l = j - 1
            r = j
            res_str = ""

            res+=subLen(l, r, 0)
        
        return res