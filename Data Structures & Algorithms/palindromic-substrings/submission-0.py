class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for index in range(len(s)):

            # check for odd length substrings
            L, R = index, index
            while L >=0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            
            # check for even length substrings
            L, R = index, index + 1
            while L >=0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
        
        return count