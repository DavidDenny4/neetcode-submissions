class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visiting = set()

        def dfs(r, c, index):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visiting or index >= len(word) or board[r][c] != word[index]:
                return False

            visiting.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            visiting.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    return dfs(r, c, 0)
        return False