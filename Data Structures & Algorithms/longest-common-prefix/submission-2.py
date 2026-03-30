class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs[0]) == 0:
            return ""
        
        res = ""

        curr_idx = 0

        while True:
            if curr_idx > len(strs[0]) - 1:
                break
            curr_char = strs[0][curr_idx]
            i = 1
            while i < len(strs):
                if curr_idx > len(strs[i]) - 1 or strs[i][curr_idx] != curr_char:
                    break
                i+=1
            if i != len(strs):
                break
            res+=curr_char
            curr_idx+=1
        
        return res
