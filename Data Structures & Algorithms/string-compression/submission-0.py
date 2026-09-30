class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        L, R = 0, 0
        while R < len(chars):
            if chars[L] == chars[R]:
                R += 1
            if chars[L] != chars[R]:
                count += 1
                L = R
        count += 1
        return count