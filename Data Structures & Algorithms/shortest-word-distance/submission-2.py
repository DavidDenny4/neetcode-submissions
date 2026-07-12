class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        first = -1
        second = -1
        distance = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                first = i
            if wordsDict[i] == word2:
                second = i
            if first != -1 and second != -1:
                distance = min(distance, abs(first - second))
        return distance
