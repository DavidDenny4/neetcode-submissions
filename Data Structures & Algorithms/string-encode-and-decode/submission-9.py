class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        # Add count of words at beginning
        for s in strs:
            result = result + str(len(s)) + s

            
    def decode(self, s: str) -> List[str]:

        result = ""

        # Add count of words at beginning
        for s in strs:
            result = result + str(len(s)) + s