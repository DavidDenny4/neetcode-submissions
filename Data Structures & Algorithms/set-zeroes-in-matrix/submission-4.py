class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = [True] * len(matrix)
        cols = [True] * len(matrix[0])

        # set map of rows and cols to False if 0 is present in any of them
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r], cols[c] = False, False
                
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if not rows[r] or not cols[c]:
                    matrix[r][c] = 0
        
        return