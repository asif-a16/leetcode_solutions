class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_group = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagram_group[key].append(word)

        return list(anagram_group.values())
