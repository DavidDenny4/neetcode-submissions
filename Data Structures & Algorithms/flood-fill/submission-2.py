class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(matrix, row, col):
            ROWS = len(matrix)
            COLS = len(matrix[0])

            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return matrix

            if matrix[row][col] == original:
                matrix[row][col] = color

                dfs(matrix, row + 1, col)
                dfs(matrix, row - 1, col)
                dfs(matrix, row, col + 1)
                dfs(matrix, row, col - 1)

                return matrix
            else:
                return matrix 
            
        original = image[sr][sc]

        return dfs(image, sr, sc)    
        
            
            
