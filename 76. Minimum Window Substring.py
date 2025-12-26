class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_count, window = {}, {}

        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right+1] if res_len != float("inf") else ""
