class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        size = 0
        seen = set()
        for R in range(len(s)):
            if s[R] in seen:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
            size = max(size, R - L + 1)
            seen.add(s[R])
        return size
            