class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        return abs(wordsDict.index(word2) - wordsDict.index(word1))