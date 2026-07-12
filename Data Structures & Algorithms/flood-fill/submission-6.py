class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(matrix, row, col):

            ROWS = len(matrix)
            COLS = len(matrix[0])

            if row < 0 or col < 0 or row >= ROWS or col >= COLS or matrix[row][col] == color:
                return matrix

            if matrix[row][col] == original_color:
                matrix[row][col] = color

                matrix = dfs(matrix, row + 1, col)
                matrix = dfs(matrix, row - 1, col)
                matrix = dfs(matrix, row, col + 1)
                matrix = dfs(matrix, row, col - 1)

            return matrix    
        
        original_color = image[sr][sc]
        return dfs(image, sr, sc)
