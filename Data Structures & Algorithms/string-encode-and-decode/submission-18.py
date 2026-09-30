class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        for i in range(len(s)):
            length = ""
            print(length)
            if s[i] != "#":
                length = length + s[i]
            else:
                length = int(length)
                result.append(s[i + 1, i + 1 + length])
                i += (1 + length)
                length = ""
        
        return result
