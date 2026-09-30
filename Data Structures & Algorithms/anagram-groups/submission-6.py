class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            print(sorted(word))
            anagrams[sort(word)].append(word)
        return anagrams.values()