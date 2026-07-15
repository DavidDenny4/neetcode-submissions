class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, index, visited, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[index]:
                return False
            
            if index == len(word) - 1:
                return board[r][c] == word[index]
            
            visited.add((r, c))
            directions = [(1, 0), (-1 , 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1, visited, word):
                    return True
            visited.remove((r,c))
            return False
        
        res = []
        for word in words:
            visited = set()
            for r in ROWS:
                for c in COLS:
                    if board[r][c] == word[0] and dfs(r, c, 0, word):
                        if word not in res:
                            res.append(word)
        return res