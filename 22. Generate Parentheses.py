class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def is_valid(brackets: str) -> bool:
            stack = []
            for char in brackets:
                if char == "(":
                    stack.append("(")
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
            return not stack

        def dfs(path: str):
            if len(path) >= 2 * n:
                if is_valid(path):
                    result.append(path[:])
                return
            
            dfs(path + "(")
            dfs(path + ")")

        dfs("")

        return result
