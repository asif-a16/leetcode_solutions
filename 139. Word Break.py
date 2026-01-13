class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * len(s) + 1
        cache[len(s)] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    cache[i] = cache[i + len(word)]
                if cache[i]:
                    break

        return cache[0]
