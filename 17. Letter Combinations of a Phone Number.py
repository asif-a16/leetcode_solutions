class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result: list[str] = []
        sett = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        def dfs(i: int, substring: list[str]):
            if i == len(digits):
                result.append("".join(substring))
                return
            
            letters = sett[digits[i]]
            for letter in letters:
                substring.append(letter)
                dfs(i + 1, substring)
                substring.pop()

        dfs(0, [])
        return result
