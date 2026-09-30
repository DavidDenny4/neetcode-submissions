class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, dist):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) or grid[r][c] == -1:
                return
            
            if grid[r][c] == 2147483647:
                grid[r][c] = dist
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, dist + 1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
            
            

            


