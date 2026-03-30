class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = defaultdict(int)

        for i in range(len(s)):
            ends[s[i]] = i
        
        curr_end = ends[s[0]]
        res = []
        left = -1
        for i in range(len(s)):
            if ends[s[i]] > curr_end:
                curr_end = ends[s[i]]
            if i == curr_end:
                res.append(curr_end - left)
                left = curr_end
        
        return res
            

