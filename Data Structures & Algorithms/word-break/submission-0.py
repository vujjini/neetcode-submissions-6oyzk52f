class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # def dfs(i):
        #   whole word = (word[:i + 1] in dict)
        #   for j in range(0, i - 1):
        #       if dfs(j):
                    # if word[j:i + 1] in dict:
                        # return True
        #   return False

        cache = {}

        m = set(wordDict)

        # neetcode

        def dp(i):
            if i in cache:
                return cache[i]

            cache[i] = False
            if s[:i + 1] in m:
                cache[i] = True
            else:
                for j in range(i):
                    if dp(j):
                        if s[j + 1:i + 1] in m:
                            cache[i] = True
            return cache[i]
        
        
        res = dp(len(s) - 1)
        print(cache)

        return res
