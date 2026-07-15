class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        ROWS = len(matrix)
        COLS = len(matrix[0])
        L, R = 0, (ROWS * COLS) - 1
        
        while L <= R:
            mid = (L + R) // 2
            row, col = mid // ROWS, mid % COLS
            if matrix[row][col] < target:
                L = mid + 1
            elif matrix[row][col] > target:
                R = mid - 1
            else: 
                return True
        return False