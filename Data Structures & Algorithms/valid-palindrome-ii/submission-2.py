class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        L, R = 0, len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                count += 1
            if L == R and count > 1:
                return False
            L += 1
            R -= 1
        return True if count < 2 else False