class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            for i in range(len(s) / 2):
                if s[i] != s[-i]:
                    return False
            return True