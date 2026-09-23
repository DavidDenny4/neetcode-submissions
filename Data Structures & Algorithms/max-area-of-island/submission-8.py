class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        max_count = 0
        visited = set()


        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r,c))
            count = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                    count += dfs(r + dr, c + dc)
            
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                max_count = max(max_count, dfs(r, c))
        
        return max_count
