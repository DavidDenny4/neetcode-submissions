class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])        

        print(f"matrix before is {matrix}")
        for r in ROWS:
            for c in COLS:
                if matrix[r][c] == 0:
                    matrix[r] = [0] * COLS
                    matrix[c] = [0] * ROWS

        print(f"matrix after is {matrix}")

        return matrix
                