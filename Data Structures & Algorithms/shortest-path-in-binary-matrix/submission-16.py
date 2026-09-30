class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        length = 0
        visited = set()
        queue = deque()
        queue.append((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                visited.add((r,c))
                directions = [(0,1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]
                for dr, dc in directions:
                    if (r + dr, c + dc) in visited or (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or grid[(r + dr)][(c + dc)] == 1:
                        continue
                    else:
                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                
            length += 1
        
        return length if length > 0 else -1
            
