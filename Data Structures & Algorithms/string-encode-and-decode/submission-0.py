class Solution:

    def encode(self, strs: List[str]) -> str:
        # combine all the strings, get length of all the strings,
        # save its length as l.
        # and append length of each string to the current string.
        s = ""
        for i in strs:
            s = s + chr(len(i)) + i
        # l = len(s)
        # s = s + chr(l)
        # for i in str:
        #     s = s + chr(len(i))
        return s

    def decode(self, s: str) -> List[str]:
        # separate substrings before l and after l.
        # the second sub string convert each character into int
        # and loop through the first substring that many times and add the word to
        # the output.
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







