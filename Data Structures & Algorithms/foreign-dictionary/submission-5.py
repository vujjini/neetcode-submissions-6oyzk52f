class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # create an adj list
        # create an indegree map

        if len(words) == 1:
            return words[0]
        
        res = []

        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()
        indegree = defaultdict(int)

        prev = words[0]

        for i in range(1, len(words)):
            curr = words[i]
            x, y = 0, 0
            while x < len(prev) and y < len(curr):
                if prev[x] != curr[y]:
                    if curr[y] not in adj[prev[x]]:
                        adj[prev[x]].add(curr[y])
                        indegree[curr[y]]+=1
                    break
                x+=1
                y+=1
            if x >= len(prev) or y >= len(curr):
                if x < len(prev):
                    return ""
                continue
            prev = words[i]
        
        q = deque()
        for char in adj:
            if char not in indegree:
                q.append(char)
        

        while q:
            top = q.popleft()
            for neighbor in adj[top]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            res.append(top)
            
        return "".join(res) if len(res) == len(adj) else ""


        # a: [b]
        # b: [c]  ind = 0
        # c: []   ind = 0
        # d: []
        # e: []

        
        # a, d, e, b, c

