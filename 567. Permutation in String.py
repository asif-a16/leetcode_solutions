from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count = defaultdict(int)
        for char in s1:
            count[char] += 1

        for right in range(len(s2)):
            if right - left + 1 > len(s1):
                if s2[left] in count:
                    count[s2[left]] += 1
                left += 1
            if s2[right] in count:
                count[s2[right]] -= 1
            if max(count.values()) == 0:
                return True

        return False
