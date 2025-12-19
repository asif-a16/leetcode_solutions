class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        n = len(height)
        for i in range(n):
            if height[i] == 0:
                continue

            for j in range(i + 1, n):
                if height[j] == 0:
                    continue

                width = j - i
                if width < math.ceil(best / height[i]):
                    continue

                area = width * min(height[i], height[j])
                best = max(best, area)

        return best
