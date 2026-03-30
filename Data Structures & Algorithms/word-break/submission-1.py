class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        m = set(wordDict)

        dp = [False for i in range(len(s))]

        for i in range(len(s)):
            # if i == 0:
            #     if s[i] in m:
            #         dp[i] = True
            #         continue
            if s[:i + 1] in m:
                dp[i] = True
                continue
            else:
                for j in range(i):
                    if dp[j]:
                        if s[j + 1:i + 1] in m:
                            dp[i] = True
                            break
        print(dp)
        return dp[-1]
