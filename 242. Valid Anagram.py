class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        working = [ord(letter) for letter in s]
        for letter in t:
            if ord(letter) in working:
                working.remove(ord(letter))
            else:
                return False
        return True
