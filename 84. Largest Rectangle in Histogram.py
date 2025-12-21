class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][0]:
                stack_height, stack_idx = stack.pop()
                max_area = max(max_area, stack_height * (idx - stack_idx))
                start = stack_idx

            stack.append((height, start))
            
        for height, start in stack:
            max_area = max(max_area, ((len(heights) - start) * height))

        return max_area
