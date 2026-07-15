class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        length = 0
        root = (0, 0)
        queue = deque()
        visited = set()
        queue.append(root)
        visited.add(root)

        # BFS
        while queue:

            length += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                print(f"the current index is ({row}, {col})")
                print(f"the length currently is {length}")
                if row == ROWS - 1 and col == COLS - 1:
                    return length

                visited.add((row, col))

                directions = [(0, 1), (0, -1), (1, 0), (-1 , 0), (1, 1), (1, -1), (-1, 1), (-1 , -1)]
                for dr, dc in directions:
                    if ((row + dr) < 0 or (col+ dc) < 0 or (row + dr) >= ROWS or (col+ dc) >= COLS
                    or ((row + dr), (col+ dc)) in visited or grid[(row + dr)][(col+ dc)] == 1):
                        continue
                    else:
                        queue.append((row + dr, col + dc))
        
        return length if length > 0 and grid[ROWS - 1][COLS - 1] == 0 else -1