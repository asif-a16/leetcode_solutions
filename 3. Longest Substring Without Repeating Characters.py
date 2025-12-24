from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window = deque()
        for char in s:
            while char in window:
                window.popleft()
            window.append(char)
            max_len = max(max_len, len(window))
        return max_len
