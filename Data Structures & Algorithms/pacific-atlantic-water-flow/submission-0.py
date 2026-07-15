class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r,c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
            return
            
        for r in ROWS:
            dfs(r, 0, pacific)
            pacific.add((r,0))
            dfs(r, 0, atlantic)
            atlantic.add((r,COLS - 1))
        
        for c in COLS:
            dfs(0, c, pacific)
            pacific.add((0,c))
            dfs(0, c, atlantic)
            atlantic.add((ROWS - 1, c))

        res = []
        for r in ROWS:
            for c in COLS:
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
        
        return res

        
        
        