class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
            or (r,c) in visited or board[r][c] in ["X","T"]):
                return

            visited.add((r,c))
            if board[r][c] == "O":
                board[r][c] = "T"

            directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc) 

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0,col)
            dfs(ROWS - 1,col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
        

        