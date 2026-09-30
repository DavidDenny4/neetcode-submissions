class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_key = word.sort().join("")
            print(sorted_key)
            anagrams[sorted_key].append(word)
        return anagrams.values()