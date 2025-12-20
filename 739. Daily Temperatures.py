class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                stack_idx = stack.pop()
                answer[stack_idx] = i-stack_idx
            stack.append(i)

        return answer
