class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1) - 1
        while R < len(s2):
            if sorted(s2[L:R]) == s1_sorted:
                return True
            L += 1
            R += 1
        return False