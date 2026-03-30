class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i].isalnum() == False:
                i+=1
                continue
            if s[j].isalnum() == False:
                j-=1
                continue
            if (s[i] != s[j]):
                print(s[i], s[j])
                return False
            i+=1
            j-=1
        return True