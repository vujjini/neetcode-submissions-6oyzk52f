class Solution:
    def dfs(self, i, j):
        if i + j == len(self.s3):
            return i == len(self.s1) and j == len(self.s2)

        if (i, j) in self.dp:
            return self.dp[(i, j)]
        
        res = False
        if i < len(self.s1) and self.s1[i] == self.s3[i + j]:
            res = self.dfs(i + 1, j)
        if not res and j < len(self.s2) and self.s2[j] == self.s3[i + j]:
            res = self.dfs(i, j + 1)

        self.dp[(i, j)] = res
        return res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.dp = {}
        return self.dfs(0, 0)