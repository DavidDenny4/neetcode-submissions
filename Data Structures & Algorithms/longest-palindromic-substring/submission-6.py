class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""
        length = 0
        for index in range(len(s)):

            L, R = index, index
            sub_length = 0
            substring = ""

            # check odd length substring
            while L >= 0 and R < len(s) and s[L] == s[R]:
                # print(f"L is {L} and R is {R}")
                sub_length += 1
                substring = s[L:R + 1]
                # print(f"the current substring length is {sub_length} and substring is {substring}")
                if sub_length > length:
                    length = sub_length
                    longest = substring
                L -= 1
                R += 1
            
            # check even length substring
            L, R = index, index + 1
            sub_length = 0
            substring = ""
            while L >= 0 and R < len(s) and s[L] == s[R]:
                sub_length += 2
                substring = s[L:R + 1]
                if sub_length > length:
                    length = sub_length
                    longest = substring
                L -= 1
                R += 1
            
        return longest



