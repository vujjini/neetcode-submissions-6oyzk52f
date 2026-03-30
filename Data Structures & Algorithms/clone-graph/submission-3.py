# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # map vals (1-indexed indices) to nodes created by performing a traversal on the source (bfs). Graph is connected so we can get all the ndoes.
        # also store the originals in a list while traversingr
        # go through the list after bfs and for each pull up the corresponding copied node and set its neighbours to the neighbours of original node

        if not node:
            return None
            
        vertex_map = {}
        originals = []

        q = deque()
        visited = set()
        visited.add(node)
        q.append(node)
        originals.append(node)

        while q:
            top = q.popleft()
            print(top)
            vertex_map[top.val] = Node(top.val)
            for neighbour in top.neighbors:
                if neighbour not in visited:
                    originals.append(neighbour)
                    q.append(neighbour)
                    visited.add(neighbour)

        for vertex in originals:
            for neighbour in vertex.neighbors:
                vertex_map[vertex.val].neighbors.append(vertex_map[neighbour.val])
        
        return vertex_map[node.val]
            

