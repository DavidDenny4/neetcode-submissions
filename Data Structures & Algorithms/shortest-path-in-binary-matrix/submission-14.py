class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 0
        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))

        while queue:
            for n in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                    
                directions = [(0,1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 1), (-1, 0), (-1, -1)]
                for dr, dc in directions:
                    if (r + dr, c + dc) not in visited and not (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 1):
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                
                length += 1

        return length if length > 0 else -1