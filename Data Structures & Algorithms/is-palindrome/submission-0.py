class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowered = s.strip().lower()
        s_formatted = ""
        for c in range(len(s)):
            if s_formatted[c].isalpha():
                s_formatted = s_formatted + c
    
        L, R = 0, len(s_formatted) - 1
        while (L < R):
            if s_formatted[L] != s_formatted[R]:
                return False
            L += 1
            R -= 1
        
        return True