from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxf = 0
        answer = 1
        while right < len(s):
            window = s[left:right + 1]
            chars = set(window)
            most_frequent = 0
            for char in chars:
                most_frequent = max(most_frequent, window.count(char))

            maxf = max(maxf, most_frequent)
            if len(window) - maxf > k:
                left += 1
            else:
                right += 1

            answer = max(answer, right - left)
        
        return answer
