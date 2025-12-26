from collections import deque, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        result = ""
        matches = deque()
        count = defaultdict(int)

        for char in t:
            count[char] += 1

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1
                matches.append(right)

            if not matches:
                left += 1

            if right - left + 1 == len(t) and max(count.values()) == 0:
                return s[left:right + 1]

            while max(count.values()) <= 0:
                while left + 1 < len(s) and s[left] == s[left + 1] and count[s[left]] < 0:
                    matches.popleft()
                    count[s[left]] += 1
                    left += 1

                if right - left + 1 < len(result) or result == "":
                    result = s[left:right + 1]
                
                count[s[left]] += 1
                matches.popleft()
                left = matches[0] if matches else left

        return result
