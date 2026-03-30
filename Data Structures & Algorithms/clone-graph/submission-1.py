"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        visited = {}
        q.append(node)
        
        while q:
            curr = q.popleft()
            if curr.val not in visited:
                copy = Node(curr.val)
            else:
                copy = visited[curr.val]
            visited[curr.val] = copy
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                    visited[neighbor.val] = Node(neighbor.val)
                copy.neighbors.append(visited[neighbor.val])

        return visited[1]