class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        res = ""
        if len(strs) < 2:
            return res
        strs.sort()
        print(f"strs is {strs}")
        for i in range(len(strs[0])):
            if strs[0][:i + 1] == strs[1][:i + 1]:
                res = strs[0][:i + 1]
        return res