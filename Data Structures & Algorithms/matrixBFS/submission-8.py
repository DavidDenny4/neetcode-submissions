class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 0
        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))

        while queue:
            for i in range(len(queue)):
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for dr, dc in directions:
                    if ((row + dr, col + dc) in visited or grid[row + dr][col + dc] == 1 
                    or (row + dr) < 0 or (row + dr) >= ROWS or (col + dc) < 0 or (col + dc) >= COLS):
                        continue
                    visited.add((row + dr, col + dc))
                    queue.append((row + dr, col + dc))

            length += 1
        return -1
        
