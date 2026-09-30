class Solution:
    def numDecodings(self, s: str) -> int:
        
        vals = [int(c) for c in s]
        dp = [None] * (len(s) + 1)

        def dfs(index):

            if dp[index] is not None:
                return dp[index]

            if index == len(s):
                return 1
            
            if vals[index] == 0:
                return 0
            
            count = 0
            count += dfs(index + 1)
            if ((index + 1) < len(s) and vals[index] in [1,2] 
            and vals[index + 1] in [1,2,3,4,5,6]):
                count += dfs(index + 2)

            return count             
        
        return dfs(0)