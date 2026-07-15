class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        length = ""
        for i in range(len(s)):
            if s[i] != "#":
                length = length + s[i]
            else:
                size = int(length)
                result.append(s[i + 1, i + 1 + size])
                i += (1 + size)
                length = ""
        
        return result
