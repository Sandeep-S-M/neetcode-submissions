class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in range(len(s)):
            if ('A' <= s[i] and s[i] <= 'Z') or ('a' <= s[i] and s[i]<='z') or ('0' <= s[i] and s[i] <= '9'):
                new_str += s[i].lower()

        for i in range(len(new_str)//2):
            if new_str[i] != new_str[len(new_str)-i-1]:
                return False
        return True
