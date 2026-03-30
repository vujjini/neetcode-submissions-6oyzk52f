class Solution:
    def dfs(self, o, c, st, s):
        if o == 0 and c == 0:
            self.res.append(s)
            return
        
        if o > 0:
            self.dfs(o - 1, c, st + ['('], s + '(')
        if c > 0 and len(st) > 0:
            self.dfs(o, c - 1, st[:len(st) - 1], s + ')')
        

    def generateParenthesis(self, n: int) -> List[str]:
        # recursion + stack
        # two var, o and c denoting number of open and closing brackets left
        # recurrence relation: dfs(o, c, stack) -> dfs(o - 1, c, stack.append('('), str+='('), dfs(o, c - 1, stack.pop(), str+=')')
        # only use the opening if o > 0, only use the closing if c > 0 and stack.top() == '('
        self.res = []

        self.dfs(n, n, [], "")

        return self.res