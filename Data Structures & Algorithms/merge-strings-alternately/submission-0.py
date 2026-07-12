class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = 0
        res = []
        while L < len(word1) and L < len(word2):
            res.append(word1[L])
            res.append(word2[L])
            L += 1
        while L < len(word1):
            res.append(word1[L])
            L += 1
        while L < len(word2):
            res.append(word2[L])
            L += 1
        return "".join(res)