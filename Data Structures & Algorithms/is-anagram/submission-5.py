class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sort(s)
        sorted_t = sort(t)
        return sorted_s == sorted_t