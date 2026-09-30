class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(grid, row, col, visited):
            if row == (ROWS - 1) and col == (COLS - 1):
                return 1
            
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row,col) in visited or grid[row][col] == 1:
                return 0
            
            count = 0
            visited.add((row, col))
            count += dfs(grid, row + 1, col, visited)
            count += dfs(grid, row - 1, col, visited)
            count += dfs(grid, row, col + 1, visited)
            count += dfs(grid, row, col - 1, visited)
            visited.remove((row, col))

            return count
        
        return dfs(grid, 0, 0, visited)