class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            chr_count = [0 for i in range(26)]
            for char in word:
                chr_count[ord(char) - ord('a')]+=1
            anagrams[tuple(chr_count)].append(word)
        
        return list(anagrams.values())