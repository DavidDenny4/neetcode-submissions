class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[-1] for m in range(n) for i in range(m)]
        
        def dfs(r, c):

            if r >= m or c >= n:
                return 0
            print(f"{r}, {c}")
            if cache[r][c] != -1:
                return cache[r][c]

            if r == (m - 1) and c == (n - 1):
                return 1

            count = 0
            count += dfs(r + 1, c)
            count += dfs(r, c + 1)
            cache[r][c] = count
            return count
        
        return dfs(0,0)