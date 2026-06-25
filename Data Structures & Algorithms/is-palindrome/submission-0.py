import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        if (s2[::-1]).lower() == s2.lower():
            return True
        else:
            return False
        