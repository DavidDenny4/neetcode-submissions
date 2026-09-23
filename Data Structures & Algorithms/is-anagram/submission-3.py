class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for i in s:
            count1[ord(i) - ord('a')] += 1
        for m in t:
            count2[ord(m) - ord('a')] += 1
        return (count1 == count2)
        
