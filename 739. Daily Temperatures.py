class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and len(stack) >= 1:
                if stack[-1][0] < temperatures[i]:
                    lower_idx = stack[-1][1]
                    answer[lower_idx] = i-lower_idx
                    stack.pop()
                    continue
                break
            stack.append((temperatures[i], i))

        return answer
