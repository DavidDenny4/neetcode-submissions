class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        L, R = 0, ROWS * COLS - 1
        print(f"ROWS is {ROWS}, COLS is {COLS}, L is {L}, R is {R}")

        def get_val(index):
            row = index % ROWS
            col = index % COLS
            return matrix[row][col]
            

        while L < R:
            mid = (L + R) // 2
            if get_val(mid) == target:
                return True
            elif get_val(mid) < target:
                L = mid + 1
            elif get_val(mid) > target:
                R = mid - 1
        return False
            
