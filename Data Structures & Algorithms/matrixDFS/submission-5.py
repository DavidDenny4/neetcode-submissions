class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 1:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                count += dfs(dr, dc)
            visited.remove((r,c))

            return count
        
        return dfs(0, 0)