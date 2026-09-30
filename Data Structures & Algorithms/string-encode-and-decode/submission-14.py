class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        # Add count of words at beginning
        for s in strs:
            result = result + str(len(s)) + s
        
        print(result)
        return result

            
    def decode(self, s: str) -> List[str]:

        results = []
        for i in range(0, len(s)):
            length_str = int(s[i])
            print(length_str)
            word = s[i + 1: i + 1 + length_str]
            print(word)
            results.append(word)
            i += (1 + length_str)
            print(i)
            print(s[i])
        return results