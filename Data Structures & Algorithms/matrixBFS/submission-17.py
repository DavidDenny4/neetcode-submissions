class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0,0))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nextR, nextC = dr + r, dc + c
                    if ((nextR, nextC) not in visited and nextR >= 0 and 
                    nextC >= 0 and nextR < ROWS and nextC < COLS and
                    grid[nextR][nextC] == 0):
                        visited.add((nextR, nextC))
                        queue.append((nextR, nextC))
            length += 1

        return length

