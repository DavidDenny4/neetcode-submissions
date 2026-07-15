class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                length = max(length, r - l + 1)
            else:
                while s[r] in s[l:r+1]:
                    seen.remove(s[l])
                    l += 1
        return length
                