class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.count = 0
        vals = [int(c) for c in s]
        dp = [None] * (len(vals) + 1)

        def dfs(index): 

            if dp[index] is not None:
                return dp[index]

            if vals[index] == 0:
                return 0
            
            if index == len(vals):
                return 1
            
            self.count += dfs(index + 1)
            if index + 1 < len(vals) and vals[index] in [1,2] and vals[index + 1] in [1,2,3,4,5,6]:
                self.count += dfs(index + 2)

        dfs(0)
        return self.count
            


