class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {'(': ')',
        '{': '}',
        '[': ']'}
        for i in s:
            if i in d:
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                else:
                    x = st.pop()
                    if d[x] != i:
                        return False
        if len(st) > 0:
            return False
        return True
