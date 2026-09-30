class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorted_words = words.copy()
        sorted_words.sort(key=lambda x: words.index(x))
        return sorted_words == words