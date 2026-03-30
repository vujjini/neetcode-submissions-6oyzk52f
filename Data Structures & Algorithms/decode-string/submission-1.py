class Solution:
    def decodeString(self, s: str) -> str:

        
        strs = []
        nums = []
        
        i = 0

        while i < len(s):
            if s[i] >= 'a' and s[i] <= 'z':
                if not nums:
                    strs.append(s[i])
                else:
                    strs[-1]+=s[i]
                i+=1
                continue
            if s[i] >= '0' and s[i] <= "9":
                nums.append("")
                while s[i] >= '0' and s[i] <= "9":
                    nums[-1]+=s[i]
                    i+=1
                continue
            if s[i] == '[':
                i+=1
                strs.append("")
                while s[i] >= 'a' and s[i] <= 'z':
                    strs[-1]+=s[i]
                    i+=1
                continue
            if s[i] == ']':
                if len(strs) > 1:
                    top_str = strs.pop()
                    strs[-1]+=(int(nums.pop()) * top_str)
                else:
                    top_str = strs.pop()
                    strs.append(int(nums.pop()) * top_str)
                i+=1
                continue
        
        return "".join(strs)
