class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += (str(length) + string)
        return res
    def decode(self, s: str) -> List[str]:
        result = []
        for char in range(len(s)):
            if s[char].isdigit() and int(s[char]) in [0,1,2,3,4,5,6,7,8,9]:
                length = int(s[char])
                word = s[char + 1:char + 1 + length]
                result.append(word)
        return result