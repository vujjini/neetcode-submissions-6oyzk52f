class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_rep = [0 for _ in range(26)]

        for char in s1:
            s1_rep[ord(char) - ord('a')]+=1
        
        
        running_str = [0 for _ in range(26)]
        
        for i in range(len(s2)):
            running_str[ord(s2[i]) - ord('a')]+=1
            if i >= len(s1) - 1:
                if running_str == s1_rep:
                    return True
                running_str[ord(s2[i - (len(s1) - 1)]) - ord('a')]-=1
        
        return False
