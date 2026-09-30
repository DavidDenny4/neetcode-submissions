class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])        

        print(f"matrix before is {matrix}")
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r] = [0] * COLS

        print(f"matrix after is {matrix}")

        return 
                