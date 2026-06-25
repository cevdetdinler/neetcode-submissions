class Solution:
    def validPalindrome(self, s: str) -> bool:
        print(s)
        for i in range(len(s)):
            new = s[:i] + s[i+1:]
            if new == new[::-1]:
                return True
        return False