class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur += prev1
            if "10" <= s[i-1:i+1] <= "26":
                cur += prev2
            prev2, prev1 = prev1, cur

        return prev1
