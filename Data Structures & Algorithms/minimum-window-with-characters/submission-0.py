class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # set of letters contained in current window of s
        s_set = set()
        # set of letters in string t
        t_set = set(t)

        res = s
        L, R = 0, 0
        while L < len(s):
            if s[L] not in t_set:
                L += 1
            else:
                R = L
                while R < len(s):
                    if t_set in set(s[L:R + 1]) and len(s[L:R + 1]) < len(res):
                        res = s[L:R + 1]
        return res if res != s else ""

            