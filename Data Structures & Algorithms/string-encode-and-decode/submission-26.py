class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        
        result = []
        number = ""
        index = 0
        while index < len(s):
            if s[index] != "#":
                number = number + s[index]
                index += 1
            else:
                number = int(number)
                word = s[index + 1: index + 1 + number]
                result.append(word)
                index += (index + 1 + number)
                number = ""

        return result
