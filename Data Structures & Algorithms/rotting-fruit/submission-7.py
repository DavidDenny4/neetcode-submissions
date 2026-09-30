class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or (r + dr, c + dc) in visited:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            
            time += 1
        
        return time if len(visited) == (ROWS * COLS) else -1
