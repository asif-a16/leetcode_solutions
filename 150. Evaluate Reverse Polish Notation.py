class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            match char:
                case "+":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 + op2)
                case "-":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 - op2)
                case "*":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 * op2)
                case "/":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(int(op1 / op2))
                case _:
                    stack.append(int(char))
        
        return stack[0]
