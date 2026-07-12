class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = len(string)
            result = result + str(length) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        print(f'string is {s}')
        result = []
        index = 0
        while index < len(s):
            end_index = index
            while(s[end_index] != "#"):
                end_index += 1
            print(f'index is {index} and end_index is {end_index}')
            print(f'number we got is {s[index:end_index]}')
            length = int(s[index:end_index])
            result.append(s[end_index + 1 : end_index + 1 + length])
            print(f'results is {result}')
            index = end_index + 1 + length
        return result

            