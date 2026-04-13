class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        # basecase: if endword not in list -> return 0
        # create a graph (undirected) connecting each word with words of 1 letter difference
        # do a bfs to find the minimum dist
        # [*at, b*t, ba* ]
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i] + '*' + word[i + 1:]].append(word)
        
        q = deque()
        q.append(beginWord)
        res = 1
        visited = set()

        while q:
            n = len(q)
            for _ in range(n):
                top = q.popleft()
                visited.add(top)
                if top == endWord:
                    return res
                for i in range(len(top)):
                    curr_pattern = top[:i] + '*' + top[i + 1:]
                    for neighbor in patterns[curr_pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
            res+=1
        
        return 0
