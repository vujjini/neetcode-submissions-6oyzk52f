class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        
        def dfs(r, c, ocean, prev):

            if r < 0 or c < 0 or r == rows or c  == cols or (r, c) in ocean or heights[r][c] < prev:
                return
            
            ocean.add((r, c))
            curr = heights[r][c]
            dfs(r + 1, c, ocean, curr)
            dfs(r - 1, c, ocean, curr)
            dfs(r, c + 1, ocean, curr)
            dfs(r, c - 1, ocean, curr)
        
        pac = set()
        atl = set()

        for r in range(rows):
            dfs(r, 0, pac, -1)
            dfs(r, cols - 1, atl, -1)
        
        for c in range(cols):
            dfs(0, c, pac, -1)
            dfs(rows - 1, c, atl, -1)

        res = []

        for coord in pac:
            if coord in atl:
                res.append([coord[0], coord[1]])

        return res