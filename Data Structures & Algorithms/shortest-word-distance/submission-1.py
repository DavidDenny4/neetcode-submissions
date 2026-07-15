class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print(f"index of {word1} is {wordsDict.index(word1)}")
        print(f"index of {word2} is {wordsDict.index(word2)}")
        return abs(wordsDict.index(word2) - wordsDict.index(word1))