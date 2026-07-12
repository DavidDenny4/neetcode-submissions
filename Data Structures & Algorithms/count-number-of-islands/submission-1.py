class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        island_set = set()
        num_islands = 0

        # Given a island node, find all other nodes part of island
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0" or (row, col) in visited:
                return
            
            island_set.add((row,col))
            visited.add((row,col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in island_set:
                    num_islands += 1
                    dfs(row, col)
        
        return num_islands





    