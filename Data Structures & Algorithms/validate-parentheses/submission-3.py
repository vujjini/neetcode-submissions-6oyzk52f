class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}

        st = []

        for i in range(len(s)):
            if s[i] in brackets:
                st.append(s[i])
                continue
            if st:
                if s[i] != brackets[st[-1]]:
                    return False
                else:
                    st.pop()
                continue
            return False
        
        if len(st) == 0:
            return True
        return False
