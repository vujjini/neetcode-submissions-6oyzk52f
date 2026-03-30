class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = {'+', '-', '*', '/'}
        st = []
        for i in tokens:
            curr_res = 0
            if i not in s:
                st.append(int(i))
            else:
                x = st[-1]
                st.pop()
                y = st[-1]
                st.pop()
                if i == '+':
                    curr_res = y + x
                elif i == '-':
                    curr_res = y - x
                elif i == '*':
                    curr_res = y*x
                elif i == '/':
                    curr_res = int(y / x)
                print(y, x, curr_res)
                st.append(curr_res)
        return st[-1]
                
