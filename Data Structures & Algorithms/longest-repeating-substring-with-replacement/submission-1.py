class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        char_map = {}
        for R in range(len(s)):
            char_map[s[R]] = char_map.get(s[R], 0) + 1
            while (R - L + 1) - max(char_map.values()) > k:
                char_map[s[L]] -= 1
                L += 1
            longest = max(longest, R - L + 1)
        return longest