class Solution:
    def numDecodings(self, s: str) -> int:
        
        map = {}
        for i in range(26):
            map[chr(ord("A") + i)] = i + 1
        
        print(map)
        return 0
        
