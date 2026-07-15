class Solution:
    def numDecodings(self, s: str) -> int:

        self.count = 0
        vals = [int(c) for c in s]
        print(f"vals is {vals}")

        def dfs(index):
            if index >= len(s):
                return 0
            
            if vals[index] > 0:
                self.count += 1
                dfs(index + 1)
            
            if index + 1 < len(s) and vals[index + 1] >= 0 and vals[index + 1] <= 6:
                self.count += 1
                dfs(index + 2)
        
        dfs(0)
        return self.coutn
        
        
        
        
