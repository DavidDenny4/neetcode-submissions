class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            hash_map[key].append(word)
        return [hash_map[key] for key in hash_map]