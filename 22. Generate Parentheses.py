class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(path: list[str], num_left_brackets: int, num_right_brackets: int):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            
            if num_left_brackets < n:
                path.append("(")
                dfs(path, num_left_brackets + 1, num_right_brackets)
                path.pop()

            if num_right_brackets < num_left_brackets:
                path.append(")")
                dfs(path, num_left_brackets, num_right_brackets + 1)
                path.pop()

        dfs([], 0, 0)

        return result
