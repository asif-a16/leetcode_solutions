def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
            
        return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        added = {}

        for i in range(len(strs)):
            selected_word = strs[i]

            if i in added:
                continue

            temp = [selected_word]
            added[i] = True

            for j in range(i + 1, len(strs)):
                current_word = strs[j]
                
                if j in added:
                    continue

                if isAnagram(selected_word, current_word):
                    temp.append(current_word)
                    added[j] = True
            
            res.append(temp)

        return res
