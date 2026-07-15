class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        def dfs(index):

            if index == len(s):
                return True

            if dp[index]:
                return True
            
            for word in wordDict:
                if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                    if dfs(index + len(word)):
                        dp[index] = True
                        return True
            
            return False
            
        
        return dfs(0)