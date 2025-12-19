class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = {"(", "[", "{"}
        for char in s:
            if char in open_bracket:
                stack.append(char)
                continue
            
            if not stack:
                return False
            
            match char:
                case ")":
                    if stack.pop() != "(":
                        return False
                case "]":
                    if stack.pop() != "[":
                        return False
                case "}":
                    if stack.pop() != "{":
                        return False
            
        return not stack
