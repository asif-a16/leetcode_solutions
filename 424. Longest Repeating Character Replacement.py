class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        replacements_used = 0

        for char in s:
            freq[char] = freq.get(char, 0) + 1

            if freq[char] > max_freq:
                max_freq = freq[char]

            elif replacements_used < k:
                replacements_used += 1

            else:
                freq[s[left]] -= 1
                left += 1

        return max_freq + replacements_used
