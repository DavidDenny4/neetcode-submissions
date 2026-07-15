class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        for c in range(ord('A'), ord('Z') + 1):
            char_map[chr(c)] = 0
        
        print(char_map)
        return 0