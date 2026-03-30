class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        count = 0

        res = True

        while l < r:
            if s[l] != s[r]:
                if s[l + 1] == s[r] and count < 1:
                    l+=2
                    r-=1
                    count+=1
                    continue
                else:
                    res = False
                    break
            else:
                l+=1
                r-=1
        if not res:
            l = 0
            r = len(s) - 1
            count = 0

            res = True

            while l < r:
                if s[l] != s[r]:
                    if s[l] == s[r - 1] and count < 1:
                        l+=1
                        r-=2
                        count+=1
                        continue
                    else:
                        res = False
                        break
                else:
                    l+=1
                    r-=1
            
        
        return res