class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        # validate if all requiried chars in substring
        def valid(s, t):
            for c in t:
                if c not in s or s[c] < t[c]:
                    return False
            return True
        
        res = ""
        s_map, t_map = {}, {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        L = 0
        for R in range(len(s)):
            s_map[s[R]] = s_map.get(s[R], 0) + 1
            if valid(s_map, t_map):
                if not res or len(s[L:R + 1]) < len(res):
                    res = s[L:R + 1]
                while valid(s_map, t_map) and L < len(s):
                    if len(s[L:R + 1]) < les(res):
                        res = s[L:R + 1]
                    s_map[s[L]] -= 1
                    L += 1

        return res
            
                    