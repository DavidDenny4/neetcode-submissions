class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create hashmap for s
        map = {}
        for char in s:
            if char in map:
                map[char] = map[char] + 1
            else:
                map[char] = 1
        # Create hashmap for t
        mapTwo = {}
        for char in t:
            if char in mapTwo:
                mapTwo[char] = mapTwo[char] + 1
            else:
                mapTwo[char] = 1
        return map == mapTwo