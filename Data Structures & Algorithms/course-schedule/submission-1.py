class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # atmost numCourses - 1 prereq
        # if len(prerequisites) > numCourses - 1:
        #     return False

        # O(n*m^(n))
        # optmized to O(n + m)
        # space: O(n + m)

        # 1 -> 2 -> 3 -> 2

        # detect if there is a cycle in the directed graph

        # create adj list
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])
            indegree[prereq[1]]+=1
        # whiel creatin the adj list, map each node with indegree
        # do a BFS on each node
            # maintain a queue
            # the queue should initially contain nodes with 0 indegree
            # in each iteration
            #   pop from queue
            #   get their neighbors and reduce their indgree if it becomes zero add it to queue
    
        # at the beginning, we initalize the queue with all 0 indgree nodes
        completed = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            top = q.popleft()
            for neighbor in adj[top]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            completed+=1

        return completed == numCourses


