class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = haystack.index(needle)
        print(f"res is {res}")
        return res