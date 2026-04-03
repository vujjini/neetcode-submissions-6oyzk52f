class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # keep track of a dictionary consisting of letters in t
        # window min length == len(t)
        # keep on adding letters to the window's dict until it matches t's dict
        # matching when letter counts in window are >= letter counts in t
        # once it does, increase the left pointer while the dict still matches
        # update the res with the curr window length
        # and keep it incrementing right pointer

        def match(currWindow, t_count):
            for char in t_count:
                if currWindow[char] < t_count[char]:
                    return False
            return True

        if len(t) > len(s):
            return ""

        res = ""
        
        t_count = Counter(t)
        currWindow = {}
        
        for char in t:
            currWindow[char] = 0
        
        l, r = 0, 0

        while r < len(s):
            if s[r] in currWindow:
                currWindow[s[r]]+=1
            while match(currWindow, t_count) and l <= r:
                if len(res) == 0 or r - l + 1 <= len(res):
                    res = s[l:r + 1]
                if s[l] in currWindow:
                    currWindow[s[l]]-=1
                l+=1
            r+=1
        
        return res
            
