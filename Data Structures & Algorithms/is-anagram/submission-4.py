from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = Counter(s)
        count2 = Counter(t)
        return count1 == count2
        