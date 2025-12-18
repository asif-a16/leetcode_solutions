class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        import math
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s_len = len(clean_text)
        l = 0
        r = s_len - 1

        for i in range(math.ceil(s_len / 2)):
            if clean_text[i] == clean_text[r - i]:
                continue
            return False
        return True
