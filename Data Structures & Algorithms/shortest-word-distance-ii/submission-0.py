class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        w1, w2 = -1, -1
        shortest = len(self.words)
        for i in range(len(self.words)):
            if self.words[i] == word1:
                w1 = i
            if self.words[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                shortest = min(shortest, abs(w1 - w2))
        return shortest
                


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
