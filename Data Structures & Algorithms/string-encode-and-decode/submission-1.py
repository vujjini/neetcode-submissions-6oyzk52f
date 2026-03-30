class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + chr(len(i)) + i
        # l = len(s)
        # s = s + chr(l)
        # for i in str:
        #     s = s + chr(len(i))
        return s

    def decode(self, s: str) -> List[str]:
        outpt = []
        i = 0
        while i < len(s):
            l = ord(s[i])
            i += 1
            x = ""
            for j in range(i, i + l):
                x = x + s[j]
            outpt.append(x)
            i = i + l
        return outpt







