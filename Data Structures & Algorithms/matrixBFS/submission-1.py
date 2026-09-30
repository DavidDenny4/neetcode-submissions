class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 0
        visited = set()
        queue = deque()
        queue.append((0, 0))
        while queue:
            node = queue.popleft()
            visited.add((row,col))
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for n in neighbors:
                r, c = n[0], n[1]
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 1 or (r, c) in visited:
                    continue
                queue.append((r,c))
            length += 1
            visited.remove((r,c))
        return -1 if length == 0 -1 else length