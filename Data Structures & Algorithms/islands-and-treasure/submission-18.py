class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        level = 0

        # find treasure chests and do bfs from them
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] not in [-1, 0] and (r,c) not in visited:
                    grid[r][c] = level
                visited.add((r,c))
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or (r + dr, c + dc) in visited:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            level += 1

        return
                
                