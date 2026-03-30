class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # def rec(i, j) 
        # -> if i == len(word1) and j == len(word2) -> just return 0
        # -> if i == len(word1) -> return len(word2) - j
        # -> if j == len(word2) -> 
        # -> if word1[i] == word2[j] -> rec(i + 1, j + 1)
        # -> else -> 1 + max(rec(i + 1, j + 1), rec(i + 1, j), rec(i, j + 1))

        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(word1) and j == len(word2):
                cache[(i, j)] = 0
            elif i == len(word1):
                cache[(i, j)] = len(word2) - j
            elif j == len(word2):
                cache[(i, j)] = len(word1) - i
            elif word1[i] == word2[j]:
                cache[(i, j)] = dp(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(dp(i + 1, j + 1), dp(i + 1, j), dp(i, j + 1))
            
            return cache[(i, j)]

        return dp(0, 0)






