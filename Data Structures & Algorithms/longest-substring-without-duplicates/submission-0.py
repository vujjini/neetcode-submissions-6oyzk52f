from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)

        i = 0
        max_len = 0
        for j in range(len(s)):
            while m[s[j]] != 0:
                m[s[i]]-=1
                i+=1
            m[s[j]]+=1
            max_len = max(max_len, j - i + 1)
        
        return max_len
