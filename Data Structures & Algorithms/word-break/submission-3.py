class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)

        def dfs(index):

            if index == len(s):
                return True

            if dp[index] is not None:
                return dp[index]
            
            for word in wordDict:
                if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                    if dfs(index + len(word)):
                        dp[index] = True
                        return True
            
            dp[index] = False
            return False
            
        return dfs(0)