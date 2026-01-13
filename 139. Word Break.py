class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def dp(left: int, right: int):
            if left == right == len(s):
                return True
            
            if right == len(s):
                return False
            
            alter = False
            if s[left:right+1] in wordDict:
                if (right + 1, right + 1) in memo:
                    alter = memo[(right + 1, right + 1)]
                else:
                    memo[(right + 1, right + 1)] = dp(right + 1, right + 1)
                    alter = memo[(right + 1, right + 1)]

            if (left, right + 1) not in memo:
                memo[(left, right + 1)] = dp(left, right + 1)

            return memo[(left, right + 1)] or alter
        
        return dp(0, 0)
