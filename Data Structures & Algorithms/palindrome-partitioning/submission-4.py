class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(word):

            L, R = 0, len(word) - 1
            while L < R:
                if word[L] != word[R]:
                    return False

                L += 1
                R -= 1
            return True

        res = []
        curr_stack = []

        def dfs(index):

            print(f"current curr stack is {curr_stack}")

            if index >= len(s):
                print(f"going to add {curr_stack} to res")
                res.append(curr_stack.copy())
            
            for i in range(index + 1, len(s)):
                if is_palindrome(s[index:i]):
                    curr_stack.append(s[index:i])
                    dfs(i)
                    curr_stack.pop()
            
        dfs(0)
        return res
            
                


