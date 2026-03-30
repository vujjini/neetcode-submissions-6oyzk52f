class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        m = len(s1)
        n = len(s2)

        s1_char = [0]*26
        for char in s1:
            s1_char[ord(char) - ord('a')]+=1
        
        s2_char = [0]*26
        for char in range(m - 1):
            s2_char[ord(s2[char]) - ord('a')]+=1
        
        l = 0
        for r in range(m - 1, n):
            s2_char[ord(s2[r]) - ord('a')]+=1
            if r - l + 1 < m:
                break
            if s2_char == s1_char:
                return True
            s2_char[ord(s2[l]) - ord('a')]-=1
            l+=1
            
        return False